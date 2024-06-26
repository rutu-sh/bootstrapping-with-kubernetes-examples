# standard libraries
from datetime import datetime

# installed libraries
from pydantic import BaseModel

# custom libraries
from common import config


class User(BaseModel):
    id: str
    name: str
    email: str
    age: int


class UserRequest(BaseModel):
    name: str
    email: str
    age: int


class UserDB(BaseModel):
    id: str 
    name: str
    email: str
    age: int
    created_at: datetime
    updated_at: datetime
