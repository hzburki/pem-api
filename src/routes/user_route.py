from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", status_code=201)
def register_user():
    return {"message": "User added successfully!"}
