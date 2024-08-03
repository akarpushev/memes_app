# app/crud.py

from sqlalchemy.orm import Session
from app.models import Meme
from app.schemas import MemeCreate, MemeUpdate


def get_memes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Meme).offset(skip).limit(limit).all()


def get_meme(db: Session, meme_id: int):
    return db.query(Meme).filter(Meme.id == meme_id).first()


def create_meme(db: Session, meme: MemeCreate):
    db_meme = Meme(text=meme.text, image_url=meme.image_url)
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme


def update_meme(db: Session, meme_id: int, meme: MemeUpdate):
    db_meme = get_meme(db, meme_id)
    if db_meme:
        db_meme.text = meme.text
        db_meme.image_url = meme.image_url
        db.commit()
        db.refresh(db_meme)
    return db_meme


def delete_meme(db: Session, meme_id: int):
    db_meme = get_meme(db, meme_id)
    if db_meme:
        db.delete(db_meme)
        db.commit()
    return db_meme
