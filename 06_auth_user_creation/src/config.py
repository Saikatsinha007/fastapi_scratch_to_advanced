import os
from pydantic_settings import BaseSettings
from typing import Optional
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    DATABASE_URL: str = f"sqlite+aiosqlite:///{os.path.join(os.path.dirname(BASE_DIR), 'fastapi_db.sqlite')}"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
