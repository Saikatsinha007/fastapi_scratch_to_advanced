from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class Book(SQLModel, table=True):
    __tablename__ = "book"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=255)
    description: Optional[str] = Field(default=None)
    author: str = Field(max_length=255)
    published_year: Optional[int] = Field(default=None)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
