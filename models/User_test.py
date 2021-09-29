import enum

from pydantic import BaseModel


class Gender(str, enum.Enum):
    male: str = "male"
    female: str = "female"


class UserTest(BaseModel):
    firstname: str
    lastname: str
    gender: Gender
