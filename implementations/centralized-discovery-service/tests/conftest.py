# tests/conftest.py

import os
import sys

# Adjust the import path if necessary
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the DATABASE_URL environment variable before importing app modules
os.environ['DATABASE_URL'] = "sqlite:///:memory:"

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import create_app
from fastapi.testclient import TestClient
from app.dependencies import get_db
from app.config import settings
from app.utils.logging import setup_logging

# Setup logging for tests
setup_logging()

@pytest.fixture(scope="session")
def engine():
    """Create a new database engine for testing."""
    return create_engine(
        os.environ['DATABASE_URL'],
        connect_args={"check_same_thread": False}
    )

@pytest.fixture(scope="session")
def tables(engine):
    """Create database tables for testing."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(engine, tables):
    """Create a new database session for a test."""
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    # Rollback the transaction and close the connection after each test
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client(db_session):
    """Create a new FastAPI TestClient."""
    # Dependency override
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app = create_app()
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c