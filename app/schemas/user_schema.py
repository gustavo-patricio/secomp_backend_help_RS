from pydantic import BaseModel, ConfigDict, Field
from pydantic import UUID4
from pydantic.functional_validators import AfterValidator
from typing import Annotated, Optional
from app import auth

Password = Annotated[str | None, AfterValidator(auth.get_password_hash)]

class GetUser(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    id: UUID4
    username: str 
    password: str

class PostUser(BaseModel):
    username: str
    email: str
    password: Annotated[str, AfterValidator(auth.get_password_hash)]

class PutUser(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[Password] = None