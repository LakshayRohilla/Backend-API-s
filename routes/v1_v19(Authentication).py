"""
This endpoint will generate a JWT token for a user.  # v19(Authentication)
"""
from fastapi import FastAPI, Header
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm  # v19(Authentication)

app_v1_v19 = FastAPI(openapi_prefix="/v1_v19")

"""Our user will get a token with this token URL"""
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")

"""
# This request is a multiform request, others that we used to make are JSON requests.
# Upload photo endpoint was multipart endpoint.
Why do we do it in FastAPI, oauth 2.0 is predefined, so we can create an endpoint very easily,
This will going to be a form URL endpoint & take a form data.
It takes username and password, its predefined in fastAPI user must send both fields with this 
form request.
In this(OAuth2PasswordRequestForm = Depends()) way we took it from the user.
"""


@app_v1_v19.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    pass
