from fastapi import APIRouter

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)


@router.post("/", status_code=201)
def add_transaction():
    return {"message": "Transaction added successfully!"}
