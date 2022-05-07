from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Learning management system",
    description= "LMS for managing students and courses",
    version="0.0.1",
    contact = {
        "name":"Siam Ahmed",
        "email":"znith347@gmail.com",
    },
    license_info={
        "name":"Apache",
    },
)

class User(BaseModel):
    email : str
    is_active : bool
    bio: Optional[str]

users = []

@app.get('/users')
async def get_users():
    return users

@app.post('/users')
async def create_user(user:User):
    users.append(user)
    return {"Message":"Successfully created user"}

@app.get('/users/{id}')
async def get_user(id:int=Path(...,description="Id of the user you want to Retrieve",gt=2),q:str=Query(None,max_length=5)):
    return {"user":users[id],"query":q}