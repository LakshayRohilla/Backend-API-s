from fastapi import FastAPI, Body, Header, File
from models.author import Author
from models.user import User
from models.book import Book
from starlette.status import HTTP_201_CREATED  # v18
from starlette.responses import Response  # v18

"""I just copy pasted the imported files from run.py file """  # this whole is in v19


app_v1 = FastAPI(openapi_prefix="/v1")
"""we are going to do versioning by adding prefix to our URL."""

"""Now we are pasting all the API`s here"""


@app_v1.post("/user/status_code", status_code=HTTP_201_CREATED)
async def post_user(user: User, x_custom: str = Header(...)):
    return {"Request Body": user, "Request custom header": x_custom}


"""To post user information, [path API]"""


@app_v1.post("/user")
async def post_user(user: User):
    return {"Request Body": user}


"""Here, I`m coping above API and making changes in it for "CUSTOM HEADERS", 
as i dont want to make any changes in that."""


@app_v1.post("/user_header")
async def post_user(user: User, x_custom: str = Header(...)):
    return {"Request Body": user, "Request custom header": x_custom}


"""To get user password, [path API]"""


@app_v1.get("/user")
async def get_user_validation(password: str):
    return {"The password is": password}


"""Queried API, we`ll be sending a variable in the in the API,[queried API] """


@app_v1.get("/book/{isbn}")
async def get_book_with_isbn(isbn: str):
    return {"Changeable parameter": isbn}


"""Here, We`re trying to send model as a response but its not working for me"""  # v18
"""Sometimes we dont want to send a parameter in the response model,
lets say we wants to exclude author parameter"""


@app_v1.get("/book/{isbn}/rm", response_model=Book)
# @app.get("/book/{isbn}/rm", response_model=Book, response_model_exclude=["author"] )
# The above line is very important as we can select which attributes of the model to
# include and exclude in the response we are getting.
# async def get_book_with_isbn_and_response_model(isbn: str):
async def get_book_with_isbn_and_response_model():
    author_dict = {
        "name": "Author 1 Lakshay",
        "book": ["book1", "book2"],
    }
    author1 = Author(**author_dict)
    book_dict1 = {
        "isbn": "isbn1",
        "name": "book1",
        "year": 2019,
        "author": author1,
    }
    book1 = Book(**book_dict1)

    return book1


"""We`ll be merging path api with queried api"""


@app_v1.get("/author/{id1}/book")
async def get_author_books(id1: int, category: str, order: str = "asc"):
    return {"Parameters": order + category + str(id1)}


"""Patch(update small bit of info), we`re patching name of the author"""


@app_v1.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed=True)):
    """if you want to take a parameter in Json body, then we need to import body from fast api"""
    """Whenever we are expecting json we use Body"""
    """API realized that this name parameter is taken in the Json body."""
    return {"Name": name}


"""API takes both user and author objects in its body"""


@app_v1.post("/user/author")  # v18
async def post_user_and_author(user: User, author: Author):
    """This is what we do when we wants to take multiple parameters"""
    return {"User is:": user, "Author is :": author}


"""When we wants to take Body parameter which is not an object"""


@app_v1.post("/user/authorwithparam")
async def post_user_and_authorwithparam(user: User, author: Author,
                                        bookstore_name: str = Body(..., embed=True)):
    """This is what we do when we wants to take multiple parameters"""
    return {"User is:": user, "Author is :": author, "Bookstore_name: ": bookstore_name}


"""sometime we need file upload endpoint, lets say user can upload profile pic to the API 
Endpoint that takes a file as a byte"""  # v18
"""For running this API you have to install multipart also *pip install python-multipart*"""


@app_v1.post("/user/photo")
async def upload_user_photo(profile_photo: bytes = File(...)):
    # For this we have import File from fastAPI
    return {"File Size": len(profile_photo)}


"""API to send custom headers in our response"""  # v18


@app_v1.post("/user/photowithheader")
async def upload_user_photowithheader(response: Response, profile_photo: bytes = File(...)):
    # For this we have import File from fastAPI
    response.headers["profile-size"] = str(len(profile_photo))
    # we have made headers value as a string bcz headers can take only string values.
    response.set_cookie(key="cookie-api", value="test")
    return {"File Size": len(profile_photo)}


"""Now if we wants to request our endpoint then we have to add version 1 prefix to our request """
