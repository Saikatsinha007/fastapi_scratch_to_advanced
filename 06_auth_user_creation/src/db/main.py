from sqlmodel import SQLModel as sqlmodel, create_engine, Session, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from config import settings

connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}

sqlmodel_engine = create_engine(
    settings.DATABASE_URL.replace("+asyncpg", "").replace("+aiosqlite", ""), 
    echo=True, 
    connect_args=connect_args
)
async_engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


def get_db():
    with Session(sqlmodel_engine) as session:
        yield session


async def get_async_db():
    async with async_session_maker() as session:
        yield session
