# app/routers/discovery.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas
from app.dependencies import get_db
from app.crud.intent import get_intents_by_filters

router = APIRouter(prefix="/api/intents", tags=["Discovery"])

@router.get("/search", response_model=List[schemas.Intent])
def search_intents(
    intent_name: Optional[str] = Query(None, min_length=3),
    uid: Optional[str] = None,
    description: Optional[str] = Query(None, min_length=3),
    tags: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Search for intents based on criteria."""
    tag_list = [tag.strip() for tag in tags.split(',')] if tags else None
    intents = get_intents_by_filters(
        db=db,
        intent_name=intent_name,
        uid=uid,
        description=description,
        tags=tag_list,
        skip=skip,
        limit=limit
    )
    if not intents:
        raise HTTPException(status_code=404, detail="No intents found.")
    return intents