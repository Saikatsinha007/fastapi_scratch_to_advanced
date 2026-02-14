from fastapi import APIRouter, status, Depends, HTTPException
from .schemas import BookCreateModel, BookResponseModel, BookUpdateModel
from .service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from typing import List

book_router = APIRouter()
book_service = BookService()

@book_router.get("/", response_model=List[BookResponseModel])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.get("/{book_uid}", response_model=BookResponseModel)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)):  # Changed to str
    book = await book_service.get_book(book_uid, session)
    
    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

@book_router.post("/", response_model=BookResponseModel, status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book_data, session)
    return new_book

@book_router.patch("/{book_uid}", response_model=BookResponseModel)
async def update_book(
    book_uid: str,  # Changed to str
    update_data: BookUpdateModel, 
    session: AsyncSession = Depends(get_session)
):
    updated_book = await book_service.update_book(book_uid, update_data, session)
    
    if updated_book:
        return updated_book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):  # Changed to str
    deleted = await book_service.delete_book(book_uid, session)
    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    
    return None