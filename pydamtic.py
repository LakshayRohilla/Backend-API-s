import datetime
from pydantic import BaseModel


class Book(BaseModel):
    """We are making class(object type) that we can use as a variable type later on in the functions."""
    """For example : def print_book(book: Book[this is the object type we are making below]):"""
    """We used BaseModel for the validation"""
    name: str
    price: float = 10.0
    year: datetime.datetime


book1 = {"name": "book1", "price": 11.9, "year": datetime.datetime.now()}
"""Here, we just made a dictionary"""

book_object = Book(**book1)
"""making object, passing dic(book1) in object, used kargs to send the dic in the object"""


def print_book(book: Book):
    """In the function parameter i send a variable "book" which is type of Book class. """
    """Mpst of the parameters have type of object"""
    print(book)


print_book(book_object)
"""Calling print_book function & sending object into the function that is containing dictionary"""




