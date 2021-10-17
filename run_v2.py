from fastapi import FastAPI
from routes.v2 import app_v2

app = FastAPI()


"""Now we have to mount our version 2 to the original app"""   # v19
"""This is same as the version 1 just the naming convention changed."""  # v19
"""NOTE:- We can put run_v1 & run_v2 files content under our original run file too, we just remove 
          all the API`s from there
          and put under v1 and v2 files and make AIP`s changes by using appropriate prefix"""

app.mount("/v2", app_v2)
