# app/schemas/tag.py

from pydantic import BaseModel, ConfigDict

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    model_config = ConfigDict(from_attributes=True)