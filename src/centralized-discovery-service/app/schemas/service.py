# app/schemas/service.py

from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from .intent import Intent, IntentCreate

class ServiceBase(BaseModel):
    name: str
    description: str
    service_url: str
    service_logo_url: Optional[str] = None
    service_terms_of_service_url: Optional[str] = None
    service_privacy_policy_url: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class ServiceCreate(ServiceBase):
    model_config = ConfigDict(from_attributes=True)
    pass

class ServiceUpdate(BaseModel):
    description: Optional[str] = None
    service_url: Optional[str] = None
    service_logo_url: Optional[str] = None
    service_terms_of_service_url: Optional[str] = None
    service_privacy_policy_url: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class Service(ServiceBase):
    id: int
    intents: List[Intent] = []
    model_config = ConfigDict(from_attributes=True)

class ServiceInfo(ServiceBase):
    model_config = ConfigDict(from_attributes=True)
    pass

class AgentsJson(BaseModel):
    service_info: ServiceInfo
    intents: List[IntentCreate]
    model_config = ConfigDict(from_attributes=True)