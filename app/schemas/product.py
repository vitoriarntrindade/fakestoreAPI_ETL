from pydantic import BaseModel
from datetime import datetime


class ProductBase(BaseModel):
    """Base schema for a product."""

    name: str
    category: str
    price: float
    description: str
    image_url: str


class ProductCreate(ProductBase):
    """Schema for creating a new product."""
    pass


class ProductResponse(ProductBase):
    """Schema for returning a product in API responses."""

    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
