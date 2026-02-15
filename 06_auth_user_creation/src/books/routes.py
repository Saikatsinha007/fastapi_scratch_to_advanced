from typing import List
from fastapi import APIRouter, HTTPException, status
from books.schemas import BookCreate, BookUpdate, BookResponse
from books.service import BookService

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=List[BookResponse])
def get_books(skip: int = 0, limit: int = 100):
    books = BookService.get_all_books(skip=skip, limit=limit)
    return books


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    book = BookService.get_book_by_id(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    book = BookService.create_book(
        title=book_data.title,
        description=book_data.description,
        author=book_data.author,
        published_year=book_data.published_year
    )
    return book


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookUpdate):
    book = BookService.update_book(
        book_id=book_id,
        title=book_data.title,
        description=book_data.description,
        author=book_data.author,
        published_year=book_data.published_year
    )
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    success = BookService.delete_book(book_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return None
