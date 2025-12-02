from typing import List

from fastapi import APIRouter

from models.order_model import Order, OrderCreate, OrderUpdate
from services.order_service import (create_order, delete_order, get_all_orders,
                                    get_order_by_id, update_order)
from utils.exceptions import raise_not_found
from utils.responses import created_response, success_response

router = APIRouter(prefix="/orders", tags=["Orders"])


# Get all orders
@router.get("/", response_model=List[Order])
async def read_orders():
    orders = await get_all_orders()
    return success_response(
        [o.dict() for o in orders], message="Orders fetched successfully"
    )


# Get order by ID
@router.get("/{order_id}", response_model=Order)
async def read_order(order_id: str):
    order = await get_order_by_id(order_id)
    return success_response(order.dict(), message="Order fetched successfully")


# Create new order
@router.post("/", response_model=Order)
async def add_order(order: OrderCreate):
    created = await create_order(order)
    return created_response(created.dict(), message="Order created successfully")


# Update order
@router.put("/{order_id}", response_model=Order)
async def edit_order(order_id: str, new_data: OrderUpdate):
    updated = await update_order(order_id, new_data)
    return success_response(updated.dict(), message="Order updated successfully")


# Delete order
@router.delete("/{order_id}", response_model=Order)
async def remove_order(order_id: str):
    deleted = await delete_order(order_id)
    return success_response(deleted.dict(), message="Order deleted successfully")
