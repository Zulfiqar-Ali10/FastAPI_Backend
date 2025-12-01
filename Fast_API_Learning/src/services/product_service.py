from typing import List, Optional
from models.product_model import Product, ProductCreate, ProductUpdate

# In-memory DB
products_db: List[Product] = []

def get_all_products() -> List[Product]:
    return products_db  

def get_product_by_id(product_id: int) -> Optional[Product]:
    return next((p for p in products_db if p.id == product_id), None)

def create_product(product_data: ProductCreate) -> Product:
    if get_product_by_id(product_data.id):
        raise ValueError(f"Product with ID {product_data.id} already exists")
    product = Product(**product_data.dict())
    products_db.append(product)
    return product

def update_product_partial(product_id: int, updated_fields: ProductUpdate) -> Product:
    """PATCH: partial update"""
    product = get_product_by_id(product_id)
    if not product:
        raise ValueError(f"Product with ID {product_id} not found")
    updated_data = updated_fields.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(product, key, value)
    return product

def update_product_full(product_id: int, new_product: ProductCreate) -> Product:
    """PUT: full replace"""
    product = get_product_by_id(product_id)
    if not product:
        raise ValueError(f"Product with ID {product_id} not found")
    # Replace all fields
    product.name = new_product.name
    product.price = new_product.price
    product.in_stock = new_product.in_stock
    return product

def delete_product(product_id: int) -> Product:
    product = get_product_by_id(product_id)
    if not product:
        raise ValueError(f"Product with ID {product_id} not found")
    products_db.remove(product)
    return product
