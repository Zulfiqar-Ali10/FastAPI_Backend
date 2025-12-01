from fastapi import APIRouter, HTTPException, status
from typing import List
from models.order_model import Order, OrderCreate, OrderUpdate
from services.order_service import (
    get_all_orders,
    get_order_by_id,
    create_order,
    update_order,
    delete_order
)

router = APIRouter(prefix="/orders", tags=["Orders"])

# Get all orders
@router.get("/", response_model=List[Order])
async def read_orders():
    return await get_all_orders()

# Get order by ID
@router.get("/{order_id}", response_model=Order)
async def read_order(order_id: str):
    order = await get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return order

# Create new order
@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def add_order(order: OrderCreate):
    return await create_order(order)

# Update order
@router.put("/{order_id}", response_model=Order)
async def edit_order(order_id: str, new_data: OrderUpdate):
    updated = await update_order(order_id, new_data)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return updated

# Delete order
@router.delete("/{order_id}", response_model=Order)
async def remove_order(order_id: str):
    deleted = await delete_order(order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return deleted
