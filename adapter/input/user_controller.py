from fastapi import APIRouter, HTTPException
from application.UserService import UserService
from domain.dataclasses.user_dataclass import User
from pydantic import BaseModel
import uuid

router = APIRouter()
user_service = UserService()

class UserCreate(BaseModel):
    email: str
    username: str
    password_hash: str
    name: str
    birth_date: str
    gender: str

@router.post("/users/")
def create_user(user: UserCreate):
    user = user_service.register_user(
        email=user.email,
        username=user.username,
        password_hash=user.password_hash,
        name=user.name,
        birth_date=user.birth_date,
        gender=user.gender
    )
    return user

@router.get("/users/{user_id}")
def read_user(user_id: str):
    user = user_service.get_user(uuid.UUID(user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user 