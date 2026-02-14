from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Config(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./books.db")
    
config = Config()