from fastapi import FastAPI
from src.books.routes import router as books_router

API_VERSION = "v1"

app = FastAPI(
    title="Bookly",
    description="A RESTful API for managing books",
    version=API_VERSION,
)

app.include_router(
    books_router,
    prefix=f"/api/{API_VERSION}/books",
    tags=["Books"],
)
