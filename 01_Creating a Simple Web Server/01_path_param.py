
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


#inside main.py

#path 
@app.get('/greet/{username}')
async def greet(username:str):
   return {"message":f"Hello {username}"}
