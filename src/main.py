from fastapi import FastAPI, Response

from src.routes import transaction_route, user_route

app = FastAPI()

app.include_router(user_route.router)
app.include_router(transaction_route.router)


@app.get("/", status_code=200)
def root():
    return Response()
