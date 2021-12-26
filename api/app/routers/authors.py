from fastapi import APIRouter, HTTPException

from typing import List

from sqlmodel import select
from app.models import engine, session, Authors

router = APIRouter()

@router.post("/authors/", response_model = Authors, tags=["authors"])
def create_author(author: Authors) -> Authors:
    session.add(author)
    session.commit()
    session.refresh(author)
    return author

@router.get("/authors/", response_model = List[Authors], tags=["authors"])
def get_authors(skip: int = 0, limit: int = 100) -> List[Authors]:
    authors = session.exec(select(Authors).offset(skip).limit(limit)).all()
    return authors

@router.get("/authors/{author_id}", response_model = Authors, tags=["authors"])
def get_author(author_id: int) -> Authors:
    author = session.get(Authors, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.patch("/authors/{author_id}", response_model=Authors, tags=["authors"])
def update_author(author_id: int, author: Authors) -> Authors:
    db_author = session.get(Authors, author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    author_data = author.dict(exclude_unset=True)
    for key, value in author_data.items():
        setattr(db_author, key, value)
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author

@router.delete("/authors/{author_id}", tags=["authors"])
def delete_author(author_id: int) -> dict:
    author = session.get(Authors, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    session.delete(author)
    session.commit()
    return {"ok": True}