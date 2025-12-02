from typing import Optional

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: Optional[str]
    name: str = Field(..., example="Laptop")
    price: float = Field(..., example=1500)
    description: Optional[str] = Field(None, example="Gaming Laptop")
    in_stock: bool = True
