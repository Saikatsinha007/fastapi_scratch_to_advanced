from fastapi import APIRouter, Depends, status, HTTPException
from .schemas import UserCreateModel, UserResponseModel, UserLoginModel
from .service import UserService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .utils import verify_password

auth_router = APIRouter()
user_service = UserService()

@auth_router.post("/signup", response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)):
    email = user_data.email
    user_exists = await user_service.user_exists(email, session)
    
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with this email already exists"
        )
    
    new_user = await user_service.create_user(user_data, session)
    return new_user

@auth_router.post("/login")
async def login_user(login_data: UserLoginModel, session: AsyncSession = Depends(get_session)):
    email = login_data.email
    password = login_data.password
    
    user = await user_service.get_user_by_email(email, session)
    
    if user is not None:
        password_valid = verify_password(password, user.password_hash)
        
        if password_valid:
            return {
                "message": "Login successful",
                "user": {
                    "uid": user.uid,
                    "username": user.username,
                    "email": user.email
                }
            }
            
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
