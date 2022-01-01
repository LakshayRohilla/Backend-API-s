from fastapi import FastAPI, Body, Header, File
from routes.v1 import app_v1
from routes.v2 import app_v2


"""
In v19(Authentication) we had added two libararies too:-
1. pip install pyjwt - for jwt token
2. pip install passlib - for cryptography
"""
"""
In v19 we are making utils directory and adding const.py in it to make our project look clean
"""

app = FastAPI()

app.mount("/v1", app_v1)
app.mount("/v2", app_v2)