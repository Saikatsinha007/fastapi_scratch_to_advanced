from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.sqlite as sqlite  # Changed from postgresql to sqlite
from sqlalchemy import func, String
from datetime import datetime
import uuid

class User(SQLModel, table=True):
    __tablename__ = "user_accounts"

    uid: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        index=True,
        nullable=False
    )

    username: str = Field(nullable=False, unique=True, index=True, sa_type=String)
    first_name: str = Field(nullable=True, sa_type=String)
    last_name: str = Field(nullable=True, sa_type=String)
    is_verified: bool = Field(default=False)
    email: str = Field(nullable=False, unique=True, index=True, sa_type=String)
    password_hash: str = Field(nullable=False, sa_type=String)
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False
    )

    def __repr__(self) -> str:
        return f"<User {self.username}>"