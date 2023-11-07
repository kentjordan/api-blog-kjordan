from fastapi import APIRouter, Depends
from models.users import CreateUser
from utils.uuid_utils import is_uuid_valid
from .users_service import create_user, delete_user_by_id

router = APIRouter(prefix="/users")


@router.post("/", status_code=200)
def create(body: CreateUser):
    return create_user(body)


@router.delete("/{id}", status_code=200)
def delete_by_id(validated_id: str = Depends(is_uuid_valid)):
    return delete_user_by_id(validated_id)
