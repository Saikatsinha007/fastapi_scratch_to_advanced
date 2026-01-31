from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dummy user data
user_list = [
    "Jerry",
    "Joey",
    "Phil"
]

@app.get("/")
async def root():
    return {"message": "FastAPI is running 🚀"}

@app.get("/search")
async def search_for_user(username: str):
    if username in user_list:
        return {"message": f"Details for user {username}"}
    
    # If user not found
    raise HTTPException(
        status_code=404,
        detail="User Not Found"
    )
