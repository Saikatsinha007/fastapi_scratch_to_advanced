from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = None
    author: str = Field(min_length=1, max_length=255)
    published_year: Optional[int] = Field(ge=1000, le=9999)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    author: Optional[str] = Field(None, min_length=1, max_length=255)
    published_year: Optional[int] = Field(None, ge=1000, le=9999)


class BookResponse(BookBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
