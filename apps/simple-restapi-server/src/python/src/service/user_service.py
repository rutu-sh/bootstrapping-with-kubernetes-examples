# standard libraries
import uuid
from typing import List

# installed libraries

# custom libraries
from models import models
from common import common
from repository import user_repository

_logger = common.get_logger("service.users")

def create_user(user: models.UserRequest) -> models.UserResponse:
    _logger.info("Creating user...")
    user_create = models.User(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        age=user.age
    )
    user_db = user_repository.create_user(user_create)
    response = models.UserResponse(
        id=user_db.id,
        name=user_db.name,
        email=user_db.email,
        age=user_db.age,
        created_at=user_db.created_at,
        updated_at=user_db.updated_at
    )
    _logger.info("User created")
    return response


def get_users() -> List[models.UserResponse]:
    _logger.info("Getting users...")
    users_db = user_repository.get_users()
    users = [
        models.UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        for user in users_db
    ]
    _logger.info("Got users")
    return users


def get_user_by_id(user_id: str) -> models.UserResponse:
    _logger.info("Getting user by id...")
    user_db = user_repository.get_user_by_id(user_id)
    user = models.UserResponse(
        id=user_db.id,
        name=user_db.name,
        email=user_db.email,
        age=user_db.age,
        created_at=user_db.created_at,
        updated_at=user_db.updated_at
    )
    _logger.info("Got user by id")
    return user


def update_user_by_id(user_id: str, user: models.UserRequest) -> models.UserResponse:
    _logger.info("Updating user by id...")
    user_update = models.User(
        id=user_id,
        name=user.name,
        email=user.email,
        age=user.age
    )
    user_db = user_repository.update_user_by_id(user_update)
    response = models.UserResponse(
        id=user_db.id,
        name=user_db.name,
        email=user_db.email,
        age=user_db.age,
        created_at=user_db.created_at,
        updated_at=user_db.updated_at
    )
    _logger.info("User updated")
    return response