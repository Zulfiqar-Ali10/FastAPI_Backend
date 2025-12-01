from fastapi import APIRouter, HTTPException, status
from typing import List
from models.product_model import Product, ProductCreate, ProductUpdate
from services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product_partial,
    update_product_full,
    delete_product
)

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[Product])
def read_products():
    return get_all_products()

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
    return product

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(product: ProductCreate):
    try:
        return create_product(product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{product_id}", response_model=Product)
def edit_product_partial(product_id: int, updated_fields: ProductUpdate):
    try:
        return update_product_partial(product_id, updated_fields)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{product_id}", response_model=Product)
def edit_product_full(product_id: int, new_product: ProductCreate):
    try:
        return update_product_full(product_id, new_product)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{product_id}", response_model=Product)
def remove_product(product_id: int):
    try:
        return delete_product(product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
