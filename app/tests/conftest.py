import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from testcontainers.mysql import MySqlContainer
from fastapi.testclient import TestClient
from app.main import app
from app.database.db import Base, get_db


@pytest.fixture(scope="session")
def engine():
    with MySqlContainer("mysql:8.0") as mysql:
        mysql.start()
        _engine = create_engine(mysql.get_connection_url().replace("mysql://", "mysql+pymysql://"))
        yield _engine


# 🔹 Criar sessão do banco de dados de teste
@pytest.fixture
def session(engine):
    Base.metadata.create_all(engine)  

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()

    yield session

    session.rollback()  
    Base.metadata.drop_all(engine)  


# 🔹 Criar um cliente de teste para FastAPI e substituir a sessão do banco
@pytest.fixture
def client(session):
    """Substitui a conexão do FastAPI para usar o banco do Testcontainers"""

    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()
