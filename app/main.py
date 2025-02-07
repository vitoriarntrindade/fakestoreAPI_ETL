from fastapi import FastAPI
from .database.db import engine, Base
from .api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FakeStore ETL API")

app.include_router(router, prefix="/api", tags=["ETL"])
