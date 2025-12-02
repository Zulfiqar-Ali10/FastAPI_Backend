import uuid

from config.db import db
from models.user_model import User, UserCreate, UserUpdate
from utils.exceptions import raise_not_found

collection = db.users


async def get_all_users():
    users = []
    async for u in collection.find():
        users.append(User(**u))
    return users


async def get_user_by_id(user_id: str):
    u = await collection.find_one({"id": user_id})
    if not u:
        raise_not_found(f"User {user_id} not found")
    return User(**u)


async def create_user(user_data: UserCreate):
    user = User(id=str(uuid.uuid4()), **user_data.dict())
    await collection.insert_one(user.dict())
    return user


async def update_user(user_id: str, update_data: UserUpdate):
    update_fields = {k: v for k, v in update_data.dict().items() if v is not None}
    if not update_fields:
        return await get_user_by_id(user_id)
    result = await collection.update_one({"id": user_id}, {"$set": update_fields})
    if result.modified_count == 0:
        raise_not_found(f"User {user_id} not found")
    return await get_user_by_id(user_id)


async def delete_user(user_id: str):
    user = await get_user_by_id(user_id)
    await collection.delete_one({"id": user_id})
    return user
