from pydantic import BaseModel, ConfigDict
from typing import Optional


class GetDonationToReceive(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    description: str
    items_type: str
    collection_point_id: int

class PostDonationToReceive(BaseModel):
    description: str
    items_type: str
    collection_point_id: int

class PutDonationToReceive(BaseModel):
    description: Optional[str] = None
    items_type: Optional[str] = None