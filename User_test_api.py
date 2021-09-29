from fastapi import FastAPI
from models.User_test import UserTest
app_test = FastAPI


@app_test.post("/testinguser")
async def user_testing_fun(user:UserTest):
    return {"Testing user API", user}

