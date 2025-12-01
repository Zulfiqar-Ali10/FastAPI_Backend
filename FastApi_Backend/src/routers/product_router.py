from fastapi import APIRouter
from typing import List
from models.product_model import Product
from services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[Product])
async def list_products():
    return await get_all_products()

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str):
    return await get_product_by_id(product_id)

@router.post("/", response_model=Product)
async def add_product(product: Product):
    return await create_product(product)

@router.put("/{product_id}", response_model=Product)
async def edit_product(product_id: str, product: Product):
    return await update_product(product_id, product.dict(exclude_unset=True))

@router.delete("/{product_id}", response_model=Product)
async def remove_product(product_id: str):
    return await delete_product(product_id)
