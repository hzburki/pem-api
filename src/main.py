from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World from Docker Container"}


@app.get('/item/{item_id}')
def read_item(item_id: int):
    return {"item_id": item_id}
