from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from services.product_service import *
from models.product_model import Product

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_products(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.post("/")
def create_new_product(product: dict, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/{product_id}")
def read_single(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(404, "Product Not Found")
    return product
