from pydantic import BaseModel
from datetime import datetime
import uuid

class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    published_date: datetime | None = None
    page_count: int | None = None
    language: str | None = None

class BookResponseModel(BaseModel):
    uid: str  # Changed from uuid.UUID to str for SQLite compatibility
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime