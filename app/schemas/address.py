from pydantic import BaseModel, UUID4
from typing import Optional

class GetAddress(BaseModel):
    id: UUID4
    street: str
    number: str
    district: str
    complement: str
    collection_point_id: int

class PostAddress(BaseModel):
    street: str
    number: str
    district: str
    complement: Optional[str] = None
    collection_point_id: int

class PutAddress(BaseModel):
    street: Optional[str] = None
    number: Optional[str] = None
    district: Optional[str] = None
    complement: Optional[str] = None
    collection_point_id: Optional[int] = None
