from sqlalchemy import Column, Integer, String, DECIMAL, Text, DateTime, func
from .db import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String(255), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
