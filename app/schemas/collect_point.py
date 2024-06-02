from pydantic import BaseModel, ConfigDict ,UUID4
from typing import Optional


class GetCollectPoint(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    name_point: str
    start_time: str
    end_time: str
    receiving_donations: bool

class PostCollectPoint(BaseModel):
    name_point: str
    start_time: str
    end_time: str
    receiving_donations: bool

class PutCollectPoint(BaseModel):
    name_point: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    receiving_donations: Optional[bool] = None


