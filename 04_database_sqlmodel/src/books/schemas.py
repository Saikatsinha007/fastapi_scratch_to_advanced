from sqlmodel import SQLModel

class BookCreate(SQLModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdate(SQLModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
