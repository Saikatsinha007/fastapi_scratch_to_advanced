from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/greet/")
async def greet(username: Optional[str] = "User"):
    return {"message": f"Hello {username}"}
# The 'username' query parameter is optional and defaults to "User" if not provided in the request URL.
