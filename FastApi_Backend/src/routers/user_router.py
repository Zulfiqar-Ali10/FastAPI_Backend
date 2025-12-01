from fastapi import APIRouter, HTTPException, status
from typing import List
from models.user_model import User, UserCreate, UserUpdate
from services.user_service import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[User])
async def read_users():
    return await get_all_users()

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def add_user(user: UserCreate):
    return await create_user(user)

@router.put("/{user_id}", response_model=User)
async def edit_user(user_id: str, new_data: UserUpdate):
    updated = await update_user(user_id, new_data)
    if not updated:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return updated

@router.delete("/{user_id}", response_model=User)
async def remove_user(user_id: str):
    deleted = await delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return deleted
