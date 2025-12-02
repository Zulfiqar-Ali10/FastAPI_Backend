from typing import List

from fastapi import APIRouter

from models.product_model import Product
from services.product_service import (create_product, delete_product,
                                      get_all_products, get_product_by_id,
                                      update_product)
from utils.responses import created_response, success_response

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=List[Product])
async def list_products():
    products = await get_all_products()
    return success_response(
        [p.dict() for p in products], message="Products fetched successfully"
    )


@router.get("/{product_id}", response_model=Product)
async def get_product_endpoint(product_id: str):
    product = await get_product_by_id(product_id)
    return success_response(product.dict(), message="Product fetched successfully")


@router.post("/", response_model=Product)
async def add_product(product: Product):
    created = await create_product(product)
    return created_response(created.dict(), message="Product created successfully")


@router.put("/{product_id}", response_model=Product)
async def edit_product(product_id: str, product: Product):
    updated = await update_product(product_id, product.dict(exclude_unset=True))
    return success_response(updated.dict(), message="Product updated successfully")


@router.delete("/{product_id}", response_model=Product)
async def remove_product(product_id: str):
    deleted = await delete_product(product_id)
    return success_response(deleted.dict(), message="Product deleted successfully")
