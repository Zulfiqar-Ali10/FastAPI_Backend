from typing import List

from fastapi import APIRouter

from models.user_model import User, UserCreate, UserUpdate
from services.user_service import (create_user, delete_user, get_all_users,
                                   get_user_by_id, update_user)
from utils.exceptions import raise_not_found
from utils.responses import created_response, success_response

router = APIRouter(prefix="/users", tags=["Users"])


# Get all users
@router.get("/", response_model=List[User])
async def read_users():
    users = await get_all_users()
    return success_response(
        [u.dict() for u in users], message="Users fetch successfully"
    )


# Get user by ID
@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = await get_user_by_id(user_id)
    return success_response(user.dict(), message="User fetched successfully")


# Create new user
@router.post("/", response_model=User)
async def add_user(user: UserCreate):
    created = await create_user(user)
    return created_response(created.dict(), message="User created successfully")


# Update user
@router.put("/{user_id}", response_model=User)
async def edit_user(user_id: str, new_data: UserUpdate):
    updated = await update_user(user_id, new_data)
    return success_response(updated.dict(), message="User updated successfully")


# Delete user
@router.delete("/{user_id}", response_model=User)
async def remove_user(user_id: str):
    deleted = await delete_user(user_id)
    return success_response(deleted.dict(), message="User deleted successfully")
