from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


class RegisterUser(BaseModel):
    email: EmailStr
    password: str


@router.post("/", status_code=201)
def register_user(req_body: RegisterUser):
    return {"message": "User added successfully!"}
