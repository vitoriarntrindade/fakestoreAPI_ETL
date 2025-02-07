import pytest
import pandas as pd
from openpyxl import load_workbook
from app.reports.excel_generator import generate_report
from app.database.db import SessionLocal


def test_excel_generation():
    db = SessionLocal()
    file_name = "products_report.xlsx"
    generate_report(db, file_name)

    # Verificar se o arquivo foi criado
    wb = load_workbook(file_name)
    assert "Produtos" in wb.sheetnames
    assert "Estatísticas" in wb.sheetnames

    # Verificar estatísticas
    ws_stats = wb["Estatísticas"]
    assert ws_stats["A1"].value == "category"
    assert ws_stats["B1"].value == "Média"
    assert ws_stats["C1"].value == "Máximo"
    assert ws_stats["D1"].value == "Mínimo"

    wb.close()
