from fastapi import FastAPI
from routes.v1 import app_v1

app = FastAPI()


"""Now we have to mount our version 1 to the original app"""

app.mount("/v1", app_v1)
