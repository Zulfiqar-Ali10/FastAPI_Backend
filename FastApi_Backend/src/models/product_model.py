from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[str]  # MongoDB ObjectId will be string
    name: str = Field(..., example="Laptop")
    price: float = Field(..., example=1500)
    description: Optional[str] = Field(None, example="Gaming Laptop")
    in_stock: bool = True
