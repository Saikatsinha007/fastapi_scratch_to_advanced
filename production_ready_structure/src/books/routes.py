from typing import List

from fastapi import APIRouter, HTTPException, status

from src.books.book_data import books
from src.books.schemas import Book, BookCreate, BookUpdate

router = APIRouter()


@router.get("/", response_model=List[Book])
def get_all_books():
    return books


@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    new_id = max(book["id"] for book in books) + 1 if books else 1

    new_book = {
        "id": new_id,
        **book.model_dump(),
    }

    books.append(new_book)
    return new_book


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.patch("/{book_id}", response_model=Book)
def update_book(book_id: int, data: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            book.update(data.model_dump())
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return
    raise HTTPException(status_code=404, detail="Book not found")
