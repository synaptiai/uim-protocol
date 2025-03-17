# app/dependencies.py

from contextlib import contextmanager

from app.database import SessionLocal


def get_db():
    """Provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
