from fastapi import FastAPI
from sqlmodel import SQLModel

from src.books.routes import router as book_router
from src.books.book_data import engine

app = FastAPI(title="Bookly with SQLModel")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(book_router, prefix="/api/v1/books", tags=["Books"])
