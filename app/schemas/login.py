from typing import Any, Annotated, Optional
from pydantic import UUID4

from pydantic import BaseModel

class PostLogin(BaseModel):
    username: str
    password: str

class ResponseLogin(BaseModel):
    token: str