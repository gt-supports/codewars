from fastapi import APIRouter

from ruslan_tasks.users.schemas import CreateUser
from ruslan_tasks.users import crud

router = APIRouter(prefix="/users", tags=["Users"])
@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)