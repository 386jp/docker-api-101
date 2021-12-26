from fastapi import APIRouter, HTTPException

from typing import List

from sqlmodel import select
from app.models import engine, session, Posts

router = APIRouter()

@router.post("/posts/", response_model = Posts, tags=["posts"])
def create_post(post: Posts) -> Posts:
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

@router.get("/posts/", response_model = List[Posts], tags=["posts"])
def get_posts(skip: int = 0, limit: int = 100) -> List[Posts]:
    posts = session.exec(select(Posts).offset(skip).limit(limit)).all()
    return posts

@router.get("/posts/{post_id}", response_model = Posts, tags=["posts"])
def get_post(post_id: int) -> Posts:
    post = session.get(Posts, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.patch("/posts/{post_id}", response_model=Posts, tags=["posts"])
def update_post(post_id: int, post: Posts) -> Posts:
    db_post = session.get(Posts, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    post_data = post.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_post, key, value)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post

@router.delete("/posts/{post_id}", tags=["posts"])
def delete_post(post_id: int) -> dict:
    post = session.get(Posts, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    session.delete(post)
    session.commit()
    return {"ok": True}