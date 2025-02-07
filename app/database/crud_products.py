from sqlalchemy.orm import Session
from .model_product import Product


def insert_products(db: Session, products: list[dict]):
    for product_data in products:
        product = Product(
            id=product_data["id"],
            name=product_data["title"],
            category=product_data["category"],
            price=product_data["price"],
            description=product_data["description"],
            image_url=product_data["image"],
            timestamp=product_data["extracted_at"]
        )
        db.merge(product)  
    db.commit()

def get_products(db: Session):
    return db.query(Product).all()
