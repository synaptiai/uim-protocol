# app/models/service.py

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Service(Base):
    """Service model representing an intent provider."""
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    service_url = Column(String, nullable=False)
    service_logo_url = Column(String, nullable=True)
    service_terms_of_service_url = Column(String, nullable=True)
    service_privacy_policy_url = Column(String, nullable=True)

    intents = relationship('Intent', back_populates='service', cascade='all, delete-orphan')