from typing import Optional
from sqlmodel import Session, select
from db.main import sqlmodel_engine
from auth.models import User
from auth.utils import get_password_hash, verify_password


class AuthService:
    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        with Session(sqlmodel_engine) as session:
            statement = select(User).where(User.email == email)
            return session.exec(statement).first()

    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        with Session(sqlmodel_engine) as session:
            statement = select(User).where(User.username == username)
            return session.exec(statement).first()

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        with Session(sqlmodel_engine) as session:
            statement = select(User).where(User.id == user_id)
            return session.exec(statement).first()

    @staticmethod
    def create_user(email: str, username: str, password: str) -> User:
        hashed_password = get_password_hash(password)
        user = User(
            email=email,
            username=username,
            password=hashed_password,
            is_active=True,
            is_superuser=False
        )
        with Session(sqlmodel_engine) as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        return user

    @staticmethod
    def authenticate_user(email: str, password: str) -> Optional[User]:
        user = AuthService.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user
