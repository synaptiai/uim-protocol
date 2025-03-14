# app/models/intent.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from app.database import Base

intent_tags = Table(
    'intent_tags',
    Base.metadata,
    Column('intent_id', Integer, ForeignKey('intents.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Intent(Base):
    """Intent model representing a single intent."""
    __tablename__ = 'intents'

    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    intent_uid = Column(String, unique=True, index=True, nullable=False)
    intent_name = Column(String, index=True, nullable=False)
    description = Column(Text)
    input_parameters = Column(JSON)
    output_parameters = Column(JSON)
    endpoint = Column(String, nullable=False)

    service = relationship('Service', back_populates='intents')
    tags = relationship('Tag', secondary=intent_tags, back_populates='intents')