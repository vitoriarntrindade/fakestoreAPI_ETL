from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.services.crud_products import ProductController
from app.schemas.product import *


router = APIRouter()

@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return ProductController.create_product(db, product)


@router.get("/products/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return ProductController.get_products(db)

