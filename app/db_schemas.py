from sqlalchemy import Column, Integer, String

from db_conn import Base, engine


class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    longitude_wgs84 = Column(String(), nullable=False)
    latitude_wgs84 = Column(String(), nullable=False)
    street = Column(String(), nullable=False)
    admarea = Column(String(), nullable=False)
    district = Column(String(), nullable=False)
    routenumbers = Column(String(), nullable=False)
    stationname = Column(String(), nullable=False)
    direction = Column(String())
    pavilion = Column(String(), nullable=False)
    operatingorgname = Column(String())
    entrystate = Column(String(), nullable=False)
    global_id = Column(Integer, nullable=False)
    geodata_center = Column(String(), nullable=False)
    geoarea = Column(String())


class Complex(Base):
    __tablename__ = 'complexes'
    id = Column(Integer, primary_key=True)
    Название_ЖК = Column(String(), nullable=False)
    Координаты_центра = Column(String(), nullable=False)


Base.metadata.create_all(engine)
