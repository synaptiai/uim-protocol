# app/models/tag.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from .intent import intent_tags

class Tag(Base):
    """Tag model for intent categorization."""
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    intents = relationship('Intent', secondary=intent_tags, back_populates='tags')