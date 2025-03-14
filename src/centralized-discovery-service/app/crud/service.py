# app/crud/service.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models, schemas
import logging

logger = logging.getLogger(__name__)

def get_service_by_name(db: Session, name: str):
    """Retrieve a service by its name."""
    return db.query(models.Service).filter(models.Service.name == name).first()

def create_service(db: Session, service_info: schemas.ServiceCreate):
    """Create a new service."""
    db_service = models.Service(
        name=service_info.name,
        description=service_info.description,
        service_url=service_info.service_url,
        service_logo_url=service_info.service_logo_url,
        service_terms_of_service_url=service_info.service_terms_of_service_url,
        service_privacy_policy_url=service_info.service_privacy_policy_url
    )
    try:
        db.add(db_service)
        db.commit()
        db.refresh(db_service)
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Integrity error creating service: {e}")
        raise
    return db_service

def update_service(db: Session, service: models.Service, updates: schemas.ServiceUpdate):
    """Update an existing service."""
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(service, key, value)
    db.commit()
    db.refresh(service)
    return service

def delete_service(db: Session, service: models.Service):
    """Delete a service and its associated intents."""
    db.delete(service)
    db.commit()