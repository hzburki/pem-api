from fastapi import FastAPI

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World from Docker Container"}


@app.get('/item/{item_id}')
def read_item(item_id: int):
    return {"item_id": item_id}
