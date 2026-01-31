from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/greet/")
async def greet(username: Optional[str] = "User"):
    return {"message": f"Hello {username}"}
