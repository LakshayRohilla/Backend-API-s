from pydantic import BaseModel
from fastapi import Query
from models.author import Author


class Book(BaseModel):
    """Tutor call this as object, *that we made a Book object*"""
    isdn: str
    name: str
    author: Author
    year: int
