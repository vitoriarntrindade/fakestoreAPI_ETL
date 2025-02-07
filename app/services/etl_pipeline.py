from sqlalchemy.orm import Session
from ..adapters.fakestore import FakeStoreAPI
from ..database.crud_products import insert_products

def run_etl(db: Session):
    products = FakeStoreAPI.fetch_products()
    print(products)
    insert_products(db, products)
    return {"message": f"{len(products)} produtos extraídos e salvos"}
