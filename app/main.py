from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserModel(BaseModel):
    username: str
    name: str 

@app.get("/user/{user_id}")
def get_user_id(user_id: str):
    # Dummy endpoint 
    return user_id

@app.post("/user/")
def get_user(user: UserModel):
    return user