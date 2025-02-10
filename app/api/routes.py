from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.db import SessionLocal, get_db
from ..database.crud_products import get_products
from ..services.etl_pipeline import run_etl
from ..reports.excel_generator import generate_report
from fastapi.responses import FileResponse


router = APIRouter()

@router.post("/products")
def start_etl(db: Session = Depends(get_db)):
    return run_etl(db)

@router.get("/products")
def list_products(db: Session = Depends(get_db)):
    return get_products(db)



@router.get("/report")
def generate_excel_report(db: Session = Depends(get_db)):
    file_name = "products_report.xlsx"
    generate_report(db, file_name)

    return FileResponse(
    file_name,
    media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    headers={"Content-Disposition": f"attachment; filename={file_name}"}
)
