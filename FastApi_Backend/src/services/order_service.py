from typing import List, Optional
from models.order_model import Order, OrderCreate, OrderUpdate
from config.db import db
import uuid

collection = db["orders"]

# Get all orders
async def get_all_orders() -> List[Order]:
    orders = []
    cursor = collection.find({})
    async for doc in cursor:
        orders.append(Order(**doc))
    return orders

# Get order by ID
async def get_order_by_id(order_id: str) -> Optional[Order]:
    doc = await collection.find_one({"id": order_id})
    if doc:
        return Order(**doc)
    return None

# Create new order
async def create_order(order_data: OrderCreate) -> Order:
    order = Order(id=str(uuid.uuid4()), **order_data.dict())
    await collection.insert_one(order.dict())
    return order

# Update order (partial or full)
async def update_order(order_id: str, update_data: OrderUpdate) -> Optional[Order]:
    update_fields = {k: v for k, v in update_data.dict().items() if v is not None}
    if not update_fields:
        return await get_order_by_id(order_id)
    result = await collection.update_one({"id": order_id}, {"$set": update_fields})
    if result.modified_count == 0:
        return None
    return await get_order_by_id(order_id)

# Delete order
async def delete_order(order_id: str) -> Optional[Order]:
    order = await get_order_by_id(order_id)
    if order:
        await collection.delete_one({"id": order_id})
        return order
    return None
