# app/routers/search.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.dependencies import get_db
from app.services.nlp import process_natural_language_query

router = APIRouter(prefix="/api/search", tags=["Search"])

@router.get("/", response_model=List[schemas.Intent])
def search_intents_by_query(
    query: str = Query(..., min_length=3),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Search intents using a natural language query."""
    intents = process_natural_language_query(db=db, query=query, skip=skip, limit=limit)
    if not intents:
        raise HTTPException(status_code=404, detail="No intents found.")
    return intents