from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.config import config

# Create async engine for SQLite
engine = create_async_engine(
    config.DATABASE_URL,
    echo=True,
    future=True,
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create async session maker
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session

# Function to initialize database (optional, but we'll use migrations instead)
async def init_db():
    async with engine.begin() as conn:
        # This is now handled by Alembic migrations
        pass