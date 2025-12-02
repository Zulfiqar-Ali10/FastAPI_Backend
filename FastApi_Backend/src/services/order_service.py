import uuid
from typing import List

from config.db import db
from models.order_model import Order, OrderCreate, OrderUpdate
from utils.exceptions import raise_not_found

collection = db.orders


async def get_all_orders() -> List[Order]:
    orders = []
    cursor = collection.find({})
    async for doc in cursor:
        orders.append(Order(**doc))
    return orders


async def get_order_by_id(order_id: str):
    doc = await collection.find_one({"id": order_id})
    if not doc:
        raise_not_found(f"Order {order_id} not found")
    return Order(**doc)


async def create_order(order_data: OrderCreate):
    order = Order(id=str(uuid.uuid4()), **order_data.dict())
    await collection.insert_one(order.dict())
    return order


async def update_order(order_id: str, update_data: OrderUpdate):
    update_fields = {k: v for k, v in update_data.dict().items() if v is not None}
    if not update_fields:
        return await get_order_by_id(order_id)
    result = await collection.update_one({"id": order_id}, {"$set": update_fields})
    if result.modified_count == 0:
        raise_not_found(f"Order {order_id} not found")
    return await get_order_by_id(order_id)


async def delete_order(order_id: str):
    order = await get_order_by_id(order_id)
    await collection.delete_one({"id": order_id})
    return order
