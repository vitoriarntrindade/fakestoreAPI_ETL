from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import *

class ProductController:
    @staticmethod
    def create_product(db: Session, produto: ProductCreate):
        db_produto = Produto(**produto.dict())
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto

    @staticmethod
    def list_products(db: Session):
        return db.query(Produto).all()
