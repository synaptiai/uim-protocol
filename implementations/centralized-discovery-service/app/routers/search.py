# app/routers/search.py

from app.dependencies import get_db
from app.services.nlp import process_natural_language_query
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/search", tags=["Search"])


@router.get("/")
def search_intents_by_query(
    query: str = Query(..., min_length=3),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    """Search intents using a natural language query."""
    intents = process_natural_language_query(db=db, query=query, skip=skip, limit=limit)
    if not intents:
        # Return empty list instead of 404 error
        return []

    # Convert SQLAlchemy objects to dictionaries
    result = []
    for intent in intents:
        intent_dict = {
            "id": intent.id,
            "service_id": intent.service_id,
            "intent_uid": intent.intent_uid,
            "intent_name": intent.intent_name,
            "description": intent.description,
            "input_parameters": intent.input_parameters,
            "output_parameters": intent.output_parameters,
            "endpoint": intent.endpoint,
            "tags": [{"name": tag.name} for tag in intent.tags] if intent.tags else [],
        }
        result.append(intent_dict)

    return result
