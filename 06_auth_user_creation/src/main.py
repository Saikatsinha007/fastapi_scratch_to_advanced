from fastapi import FastAPI
from auth.routes import router as auth_router
from books.routes import router as books_router

app = FastAPI(
    title="FastAPI Authentication",
    description="A FastAPI application with user authentication",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(books_router)


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Authentication API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
