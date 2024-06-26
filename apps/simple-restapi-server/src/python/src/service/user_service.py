# standard libraries
import uuid
from typing import List
from datetime import datetime

# installed libraries

# custom libraries
from models import models
from common import common, config
from repository import user_repository

_logger = common.get_logger("service.users")

def create_user(user: models.UserRequest) -> models.UserDB:
    _logger.info("Creating user...")
    user_db = models.UserDB(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        age=user.age,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    user_db = user_repository.create_user(user_db)
    _logger.info("User created")
    return user_db


def get_users() -> List[models.User]:
    _logger.info("Getting users...")
    users_db = user_repository.get_users()
    users = [
        models.User(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age
        )
        for user in users_db
    ]
    _logger.info("Got users")
    return users
