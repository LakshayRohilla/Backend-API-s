from pydantic import BaseModel

class JWTUser(BaseModel):
    username: str
    password: str
    disabled: bool
    # Indicates if this user is enabled or disabled.
    role: str


