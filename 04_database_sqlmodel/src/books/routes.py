from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from src.books.models import Book
from src.books.schemas import BookCreate, BookUpdate
from src.books.book_data import get_session

router = APIRouter()

@router.post("/", response_model=Book)
def create_book(
    book: BookCreate,
    session: Session = Depends(get_session),
):
    db_book = Book.from_orm(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@router.get("/", response_model=List[Book])
def get_books(session: Session = Depends(get_session)):
    statement = select(Book)
    return session.exec(statement).all()


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.patch("/{book_id}", response_model=Book)
def update_book(
    book_id: int,
    data: BookUpdate,
    session: Session = Depends(get_session),
):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in data.model_dump().items():
        setattr(book, key, value)

    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)
    session.commit()
    return {"message": "Book deleted"}
