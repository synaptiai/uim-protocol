# app/schemas/intent.py

from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from .tag import Tag

class InputParameter(BaseModel):
    name: str
    type: str
    required: bool
    description: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class OutputParameter(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class IntentBase(BaseModel):
    intent_uid: str
    intent_name: str
    description: str
    input_parameters: List[InputParameter]
    output_parameters: List[OutputParameter]
    endpoint: str
    tags: Optional[List[Tag]] = None
    model_config = ConfigDict(from_attributes=True)

class IntentCreate(IntentBase):
    pass
    model_config = ConfigDict(from_attributes=True)

class IntentUpdate(BaseModel):
    description: Optional[str] = None
    input_parameters: Optional[List[InputParameter]] = None
    output_parameters: Optional[List[OutputParameter]] = None
    endpoint: Optional[str] = None
    tags: Optional[List[Tag]] = None
    model_config = ConfigDict(from_attributes=True)

class Intent(IntentBase):
    id: int
    service_id: int
    model_config = ConfigDict(from_attributes=True)