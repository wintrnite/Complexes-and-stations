import csv
from pathlib import Path
from typing import List

from sqlalchemy import func

from constants import (
    ANSWER_CSV_HEADER,
    ANSWER_PATH,
    DISTANCE_LABEL,
    DISTORTION_COEFFICIENT,
    MAX_DISTANCE,
    SRID_3857,
    SRID_4326,
)
from db_conn import create_session
from db_schemas import Complex, Station
from models import AnswerModel


def create_answer_csv_file(ans: List[AnswerModel]):
    path = Path(ANSWER_PATH)
    with path.open('w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(ANSWER_CSV_HEADER)
        for row in ans:
            writer.writerow([row.Название_ЖК, row.name, row.distance])


def main():
    ans = []
    with create_session() as session:
        distance = (
            func.ST_Distance(
                func.ST_Transform(
                    func.ST_GeomFromGeoJSON(Station.geodata_center), SRID_3857
                ),
                func.ST_Transform(
                    func.ST_GeomFromText(Complex.Координаты_центра, SRID_4326),
                    SRID_3857,
                ),
            )
            * DISTORTION_COEFFICIENT
        )
        query = (
            session.query(
                Complex.Название_ЖК, Station.name, distance.label(DISTANCE_LABEL)
            )
            .filter(distance < MAX_DISTANCE)
            .order_by(Complex.Название_ЖК, distance)
            .all()
        )
        for row in query:
            ans.append(AnswerModel.from_orm(row))

        create_answer_csv_file(ans)


if __name__ == '__main__':
    main()
