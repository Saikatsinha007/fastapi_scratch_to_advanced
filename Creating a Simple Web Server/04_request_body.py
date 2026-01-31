from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Request Body API is running 🚀"}

# In-memory "database"
users: List[dict] = []

# -----------------------
# Request Body (Pydantic)
# -----------------------
class UserSchema(BaseModel):
    username: str
    email: str

@app.post("/create_user")
async def create_user(user_data: UserSchema):
    new_user = {
        "username": user_data.username,
        "email": user_data.email
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }

# -----------------------
# Get All Users
# -----------------------
@app.get("/users")
async def get_users():
    return users

# -----------------------
# Request Headers
# -----------------------
@app.get("/get_headers")
async def get_all_request_headers(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    referer: Optional[str] = Header(None),
    connection: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    host: Optional[str] = Header(None),
):
    return {
        "User-Agent": user_agent,
        "Accept-Encoding": accept_encoding,
        "Referer": referer,
        "Accept-Language": accept_language,
        "Connection": connection,
        "Host": host
    }
