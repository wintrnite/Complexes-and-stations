from pydantic import BaseModel


class AnswerModel(BaseModel):
    Название_ЖК: str
    name: str
    distance: str

    class Config:
        orm_mode = True
