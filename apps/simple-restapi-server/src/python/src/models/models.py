# standard libraries
import sqlalchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

# installed libraries
from pydantic import BaseModel

# custom libraries
from common import config


Base = declarative_base()


class User(BaseModel):
    id: str
    name: str
    email: str
    age: int


class UserRequest(BaseModel):
    name: str
    email: str
    age: int


class UserDB(Base):
    __tablename__ = config.DB_USER_TABLE

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now
