from fastapi import FastAPI
from app.config.db import  engine, Base
from .api import router_products

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FakeStore API")

app.include_router(products.router, prefix="/api", tags=["Products"])

@app.get("/")
def home():
    return {"message": "Welcome to FakeStore API"}
