from fastapi import FastAPI, Header

from models.user import User

from starlette.status import HTTP_201_CREATED  # v18


app_v2 = FastAPI(openapi_prefix="/v2")
"""Here, we are trying to make version 2"""  # v19


@app_v2.post("/user/status_code", status_code=HTTP_201_CREATED)
async def post_user(user: User, x_custom: str = Header(...)):
    return {"Request Body": user, "Request custom header": x_custom}
