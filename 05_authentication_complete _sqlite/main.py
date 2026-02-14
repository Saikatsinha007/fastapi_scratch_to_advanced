from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting...")
    # We're using migrations now, so init_db is not needed for table creation
    # await init_db()
    yield
    print("Server has been stopped...")

# Create FastAPI app
app = FastAPI(
    title="Book Service API",
    description="A simple CRUD API for books with user authentication (SQLite)",
    version="1.0.0",
    lifespan=life_span
)

# Include routers
app.include_router(book_router, prefix="/books", tags=["books"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Book Service API with SQLite"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}