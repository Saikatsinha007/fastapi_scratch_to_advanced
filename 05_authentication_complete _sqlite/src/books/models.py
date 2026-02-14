from sqlmodel import SQLModel, Field, Column
from sqlalchemy import String, func
from datetime import datetime
import uuid

class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        index=True,
        nullable=False
    )
    title: str = Field(sa_type=String)
    author: str = Field(sa_type=String)
    publisher: str = Field(sa_type=String)
    published_date: datetime
    page_count: int
    language: str = Field(sa_type=String)
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False
    )

    def __repr__(self) -> str:
        return f"<Book {self.title}>"