from typing import Optional

from sqlmodel import Field
from app.models import SQLModel


class Authors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    display_name: str