from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional

from api import users,courses,sections

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


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)