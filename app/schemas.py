# app/schemas.py

from pydantic import BaseModel


class MemeBase(BaseModel):
    text: str
    image_url: str


class MemeCreate(MemeBase):
    pass


class MemeUpdate(MemeBase):
    pass


class Meme(MemeBase):
    id: int

    class Config:
        from_attributes = True  # обновлено orm_mode на from_attributes
