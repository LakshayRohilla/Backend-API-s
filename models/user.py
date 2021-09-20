from pydantic import BaseModel
import enum
from fastapi import Query

"""We need to create a user class to make things easier in fast API."""
"""For Fast API, you should always think as having classes, 
since Fast API provides us auto validation and auto documentation"""
"""since it does these automatic things with data, we always tend to create classes for our objects."""


class Role(str, enum.Enum):
    """ So why do we wrote str in the Role class,
        Reason - we are describing the type of the Role(class),which is string"""
    """ * let 's think there are some predefined values for our role.
        * So we need to declare and enum types for our roles.
        * And let's say role can be just one of these two, an admin or a person.
    """

    admin: str = "admin"
    personal: str = "personal"


class User(BaseModel):
    name: str
    password: str
    mail: str = Query(..., regex="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}")
    """If we need more validation for the data we use query"""
    """... means required, and if that field is not so imp you can also write is as,
    Query(None, regex="alkaloid")"""
    role: Role
