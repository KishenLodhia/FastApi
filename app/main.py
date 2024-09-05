from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True


my_posts = []


@app.get("/")
def root():
    return {"Hello": "World World"}


@app.post("/createposts")
def create_posts(post: Post):
    return {"post": post}
