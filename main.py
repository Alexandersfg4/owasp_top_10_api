from typing import Optional
from fastapi import FastAPI
from datetime import date

from pydantic import BaseModel

app = FastAPI()

# Declare a variable as a str
# and get editor support inside the function
def main(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date

@app.get("/api/user/01")
def read_root():
    return {"id": "01",
            "email": "admin@test.com",
            "name": "Admin",
            "access": "Full"}