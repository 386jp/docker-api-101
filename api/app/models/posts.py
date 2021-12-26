from typing import Optional

from sqlmodel import Field, Relationship
from app.models import SQLModel


class Posts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author_id: Optional[int] = Field(default=None, foreign_key="authors.id")
    content: str