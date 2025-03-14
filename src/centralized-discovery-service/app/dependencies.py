# app/dependencies.py

from app.database import SessionLocal
from contextlib import contextmanager

def get_db():
    """Provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()