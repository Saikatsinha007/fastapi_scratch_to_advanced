from typing import List, Optional
from sqlmodel import Session, select
from datetime import datetime
from db.main import sqlmodel_engine
from books.models import Book


class BookService:
    @staticmethod
    def get_all_books(skip: int = 0, limit: int = 100) -> List[Book]:
        with Session(sqlmodel_engine) as session:
            statement = select(Book).offset(skip).limit(limit)
            return session.exec(statement).all()

    @staticmethod
    def get_book_by_id(book_id: int) -> Optional[Book]:
        with Session(sqlmodel_engine) as session:
            statement = select(Book).where(Book.id == book_id)
            return session.exec(statement).first()

    @staticmethod
    def create_book(title: str, description: Optional[str], author: str, published_year: Optional[int]) -> Book:
        book = Book(
            title=title,
            description=description,
            author=author,
            published_year=published_year
        )
        with Session(sqlmodel_engine) as session:
            session.add(book)
            session.commit()
            session.refresh(book)
        return book

    @staticmethod
    def update_book(book_id: int, title: Optional[str] = None, description: Optional[str] = None, 
                   author: Optional[str] = None, published_year: Optional[int] = None) -> Optional[Book]:
        with Session(sqlmodel_engine) as session:
            statement = select(Book).where(Book.id == book_id)
            book = session.exec(statement).first()
            if not book:
                return None
            
            if title is not None:
                book.title = title
            if description is not None:
                book.description = description
            if author is not None:
                book.author = author
            if published_year is not None:
                book.published_year = published_year
            
            book.updated_at = datetime.utcnow()
            session.add(book)
            session.commit()
            session.refresh(book)
        return book

    @staticmethod
    def delete_book(book_id: int) -> bool:
        with Session(sqlmodel_engine) as session:
            statement = select(Book).where(Book.id == book_id)
            book = session.exec(statement).first()
            if not book:
                return False
            session.delete(book)
            session.commit()
        return True
