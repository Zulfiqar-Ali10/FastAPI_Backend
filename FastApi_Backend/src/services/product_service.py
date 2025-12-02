from bson import ObjectId

from config.db import db
from models.product_model import Product
from utils.exceptions import raise_not_found, raise_server_error

collection = db.products


async def get_all_products():
    products = []
    async for p in collection.find():
        p["id"] = str(p["_id"])
        products.append(Product(**p))
    return products


async def get_product_by_id(product_id: str):
    product = await collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise_not_found(f"Product {product_id} not found")
    product["id"] = str(product["_id"])
    return Product(**product)


async def create_product(product: Product):
    try:
        result = await collection.insert_one(product.dict(exclude={"id"}))
        product.id = str(result.inserted_id)
        return product
    except Exception as e:
        raise_server_error(str(e))


async def update_product(product_id: str, product_data: dict):
    result = await collection.update_one(
        {"_id": ObjectId(product_id)}, {"$set": product_data}
    )
    if result.matched_count == 0:
        raise_not_found(f"Product {product_id} not found")
    return await get_product_by_id(product_id)


async def delete_product(product_id: str):
    product = await get_product_by_id(product_id)
    await collection.delete_one({"_id": ObjectId(product_id)})
    return product
