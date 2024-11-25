from typing import Union
from fastapi import FastAPI

from routers import petitionRoutes

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(petitionRoutes.router)