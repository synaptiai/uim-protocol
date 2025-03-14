# app/crud/intent.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models, schemas
import logging

logger = logging.getLogger(__name__)

def get_intent_by_uid(db: Session, intent_uid: str):
    """Retrieve an intent by its unique identifier."""
    return db.query(models.Intent).filter(models.Intent.intent_uid == intent_uid).first()

def get_intents_by_filters(
    db: Session,
    intent_name: str = None,
    uid: str = None,
    description: str = None,
    tags: list = None,
    skip: int = 0,
    limit: int = 10
):
    """Retrieve intents based on filters."""
    query = db.query(models.Intent)
    if intent_name:
        query = query.filter(models.Intent.intent_name.ilike(f"%{intent_name}%"))
    if uid:
        query = query.filter(models.Intent.intent_uid == uid)
    if description:
        query = query.filter(models.Intent.description.ilike(f"%{description}%"))
    if tags:
        query = query.join(models.Intent.tags).filter(models.Tag.name.in_(tags))
    return query.offset(skip).limit(limit).all()

def create_intent(db: Session, intent_data: schemas.IntentCreate, service_id: int):
    """Create a new intent associated with a service."""
    db_intent = models.Intent(
        service_id=service_id,
        intent_uid=intent_data.intent_uid,
        intent_name=intent_data.intent_name,
        description=intent_data.description,
        input_parameters=intent_data.input_parameters,
        output_parameters=intent_data.output_parameters,
        endpoint=intent_data.endpoint
    )
    # Handle tags
    if intent_data.tags:
        tags = []
        for tag_name in intent_data.tags:
            # Check if the tag already exists
            tag = db.query(models.Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = models.Tag(name=tag_name)
                db.add(tag)
                db.flush()  # To get the tag ID
            tags.append(tag)
        db_intent.tags = tags
    try:
        db.add(db_intent)
        db.commit()
        db.refresh(db_intent)
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Integrity error creating intent: {e}")
        raise
    return db_intent

def update_intent(db: Session, intent: models.Intent, updates: schemas.IntentUpdate):
    """Update an existing intent."""
    for key, value in updates.dict(exclude_unset=True).items():
        if key == "tags" and value is not None:
            # Update tags
            tags = []
            for tag_name in value:
                tag = db.query(models.Tag).filter(models.Tag.name == tag_name).first()
                if not tag:
                    tag = models.Tag(name=tag_name)
                    db.add(tag)
                    db.commit()
                    db.refresh(tag)
                tags.append(tag)
            intent.tags = tags
        else:
            setattr(intent, key, value)
    db.commit()
    db.refresh(intent)
    return intent

def delete_intent(db: Session, intent: models.Intent):
    """Delete an intent."""
    db.delete(intent)
    db.commit()