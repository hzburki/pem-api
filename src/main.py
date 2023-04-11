from fastapi import FastAPI

from .config.database import engine

from .models import *

user.Base.metadata.create_all(bind=engine)
wallet.Base.metadata.create_all(bind=engine)
user_wallet.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World from Docker Container"}


@app.get('/item/{item_id}')
def read_item(item_id: int):
    return {"item_id": item_id}
