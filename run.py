from fastapi import FastAPI, Body, Header
from models.author import Author
from models.user import User
from models.book import Book

"""To get "CUSTOM HEADERS" from that user we use header, we have to import those first"""
"""In FastApi we can return models as a response"""

app = FastAPI()

"""To post user information, [path API]"""


@app.post("/user")
async def post_user(user: User):
    return {"Request Body": user}


"""Here, I`m coping above API and making changes in it for "CUSTOM HEADERS", 
as i dont want to make any changes in that."""


@app.post("/user_header")
async def post_user(user: User, x_custom: str = Header(...)):
    return {"Request Body": user, "Request custom header": x_custom}


"""To get user password, [path API]"""


@app.get("/user")
async def get_user_validation(password: str):
    return {"The password is": password}


"""Queried API, we`ll be sending a variable in the in the API,[queried API] """


@app.get("/book/{isbn}")
async def get_book_with_isbn(isbn: str):
    return {"Changeable parameter": isbn}


"""Here, I`m coping above API and making changes in it for "CUSTOM HEADERS", 
as i dont want to make any changes in that."""


@app.get("/book/{isbn}", response_model=Book)
async def get_book_with_isbn(isbn: str):
    author_dict = {
        "name": "Author 1 Lakshay",
        "book": ["book1", "book2"]
    }
    author1 = Author(**author_dict)

    return {"Changeable parameter": isbn}


"""We`ll be merging path api with queried api"""


@app.get("/author/{id1}/book")
async def get_author_books(id1: int, category: str, order: str = "asc"):
    return {"Parameters": order + category + str(id1)}


"""Patch(update small bit of info), we`re patching name of the author"""


@app.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed=True)):
    """if you want to take a parameter in Json body, then we need to import body from fast api"""
    """Whenever we are expecting json we use Body"""
    """API realized that this name parameter is taken in the Json body."""
    return {"Name": name}


"""API takes both user and author objects in its body"""


@app.post("/user/author")
async def post_user_and_author(user: User, author: Author):
    """This is what we do when we wants to take multiple parameters"""
    return {"User is:": user, "Author is :": author}


"""When we wants to take Body parameter which is not an object"""


@app.post("/user/authorwithparam")
async def post_user_and_authorwithparam(user: User, author: Author, bookstore_name: str = Body(..., embed=True)):
    """This is what we do when we wants to take multiple parameters"""
    return {"User is:": user, "Author is :": author, "Bookstore_name: ": bookstore_name}


"""Since Fast API does things automatically like validation & auto-validation, we create classes for our objects."""
"""since it does these automatic things with data, we always tend to create classes for our objects."""
"""So we have a user object here, so we need to declare a user class."""
