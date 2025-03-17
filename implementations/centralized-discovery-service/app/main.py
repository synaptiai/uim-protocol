# app/main.py

from app.database import Base, engine
from app.routers import discovery, search
from app.utils.logging import setup_logging
from fastapi import FastAPI


def create_app():
    """Initialize FastAPI app and include routers."""
    app = FastAPI(title="Centralized Intent Discovery Service")

    # Set up logging
    setup_logging()

    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Include routers
    app.include_router(discovery.router)
    app.include_router(search.router)

    return app


app = create_app()
