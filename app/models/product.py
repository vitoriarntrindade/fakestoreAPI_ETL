from sqlalchemy import Column, Integer, String, DECIMAL, Text, DateTime, func
from app.config.db import Base


class Product(Base):
    """Database model for the Product entity."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(Text, nullable=True)
    timestamp = Column(DateTime, server_default=func.now())
