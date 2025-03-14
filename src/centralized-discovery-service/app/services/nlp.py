# app/services/nlp.py

import logging
from typing import List
from app.models.intent import Intent
from sqlalchemy.orm import Session
from sqlalchemy import func

logger = logging.getLogger(__name__)

def process_natural_language_query(db: Session, query: str, skip: int = 0, limit: int = 10) -> List[Intent]:
    """Process a natural language query to search for intents."""
    try:
        # Using PostgreSQL full-text search
        intents = db.query(Intent).filter(
            func.to_tsvector('english', Intent.description).match(query)
        ).offset(skip).limit(limit).all()
        return intents
    except Exception as e:
        logger.error(f"Error processing natural language query: {e}")
        return []