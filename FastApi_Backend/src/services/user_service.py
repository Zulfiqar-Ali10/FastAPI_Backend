from typing import List, Optional
from models.user_model import User, UserCreate, UserUpdate
from config.db import db
import uuid

collection = db["users"]

async def get_all_users() -> List[User]:
    users = []
    cursor = collection.find({})
    async for doc in cursor:
        users.append(User(**doc))
    return users

async def get_user_by_id(user_id: str) -> Optional[User]:
    doc = await collection.find_one({"id": user_id})
    if doc:
        return User(**doc)
    return None

async def create_user(user_data: UserCreate) -> User:
    user = User(id=str(uuid.uuid4()), **user_data.dict())
    await collection.insert_one(user.dict())
    return user

async def update_user(user_id: str, update_data: UserUpdate) -> Optional[User]:
    update_fields = {k: v for k, v in update_data.dict().items() if v is not None}
    if not update_fields:
        return await get_user_by_id(user_id)
    result = await collection.update_one({"id": user_id}, {"$set": update_fields})
    if result.modified_count == 0:
        return None
    return await get_user_by_id(user_id)

async def delete_user(user_id: str) -> Optional[User]:
    user = await get_user_by_id(user_id)
    if user:
        await collection.delete_one({"id": user_id})
        return user
    return None
