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


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    age: int
    created_at: datetime
    updated_at: datetime

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "created_at": self.created_at.strftime(config.DATETIME_FORMAT),
            "updated_at": self.updated_at.strftime(config.DATETIME_FORMAT)
        }


class UserDB(BaseModel):
    id: str 
    name: str
    email: str
    age: int
    created_at: datetime
    updated_at: datetime

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "created_at": self.created_at.strftime(config.DATETIME_FORMAT),
            "updated_at": self.updated_at.strftime(config.DATETIME_FORMAT)
        }
