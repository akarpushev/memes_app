# app/api/v1/endpoints/memes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas

from app.database import SessionLocal
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/memes", response_model=List[schemas.Meme])
def read_memes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    memes = crud.get_memes(db, skip=skip, limit=limit)
    return memes


@router.get("/memes/{id}", response_model=schemas.Meme)
def read_meme(id: int, db: Session = Depends(get_db)):
    db_meme = crud.get_meme(db, meme_id=id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme


@router.post("/memes", response_model=schemas.Meme)
def create_meme(meme: schemas.MemeCreate, db: Session = Depends(get_db)):
    return crud.create_meme(db=db, meme=meme)


@router.put("/memes/{id}", response_model=schemas.Meme)
def update_meme(id: int, meme: schemas.MemeUpdate, db: Session = Depends(get_db)):
    return crud.update_meme(db=db, meme_id=id, meme=meme)


@router.delete("/memes/{id}", response_model=schemas.Meme)
def delete_meme(id: int, db: Session = Depends(get_db)):
    return crud.delete_meme(db=db, meme_id=id)
