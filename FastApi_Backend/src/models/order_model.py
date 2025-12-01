from pydantic import BaseModel
from typing import List, Optional

class Order(BaseModel):
    id: str
    user_id: str
    products: List[str]
    total_price: float
    status: str = "pending"

class OrderCreate(BaseModel):
    user_id: str
    products: List[str]
    total_price: float

class OrderUpdate(BaseModel):
    products: Optional[List[str]] = None
    total_price: Optional[float] = None
    status: Optional[str] = None
