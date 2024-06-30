# standard libraries
import uuid
from typing import List

# installed libraries

# custom libraries
from models import models, errors
from common import common
from repository import user_repository

_logger = common.get_logger("service.users")


def create_user(user: models.UserRequest) -> models.UserResponse:
    _logger.info("creating user...")
    user_create = models.User(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        age=user.age
    )

    try:
        user_db = user_repository.create_user(user_create)
    except errors.RepositoryError as e:
        # handle repository errors
        _logger.error("error creating user", err_msg=str(e))
        if e.error_code == errors.RepositoryErrorCodes.USER_INVALID_DATA:
            raise errors.BadRequestError(errors.ServiceErrorCodes.BAD_REQUEST)
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    except Exception as e:
        # handle other errors
        _logger.error("error creating user", err_msg=str(e))
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)

    response = models.UserResponse(
        id=user_db.id,
        name=user_db.name,
        email=user_db.email,
        age=user_db.age,
        created_at=user_db.created_at,
        updated_at=user_db.updated_at
    )

    _logger.info("user created")
    return response


def get_users() -> List[models.UserResponse]:
    _logger.info("Getting users...")
    try:
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
    except errors.RepositoryError as e:
        # handle repository errors
        _logger.error("error getting users", err_msg=str(e))
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    except Exception as e:
        # handle other errors
        _logger.error("error getting users", err_msg=str(e))
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    _logger.info("Got users")
    return users


def get_user_by_id(user_id: str) -> models.UserResponse:
    _logger.info("Getting user by id...")
    try:
        user_db = user_repository.get_user_by_id(user_id)
        user = models.UserResponse(
            id=user_db.id,
            name=user_db.name,
            email=user_db.email,
            age=user_db.age,
            created_at=user_db.created_at,
            updated_at=user_db.updated_at
        )
    except errors.RepositoryError as e:
        # handle repository errors
        _logger.error("error getting user by id", err_msg=str(e))
        if e.error_code == errors.RepositoryErrorCodes.USER_NOT_FOUND:
            raise errors.NotFoundError(errors.ServiceErrorCodes.NOT_FOUND)
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    except Exception as e:
        # handle other errors
        _logger.error("error getting user by id", err_msg=str(e))
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    _logger.info("Got user by id")
    return user


def update_user_by_id(user_id: str, user: models.UserRequest) -> models.UserResponse:
    _logger.info("Updating user by id...")
    try:
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
    except errors.RepositoryError as e:
        # handle repository errors
        _logger.error("error updating user by id", err_msg=str(e))
        if e.error_code == errors.RepositoryErrorCodes.USER_NOT_FOUND:
            raise errors.NotFoundError(errors.ServiceErrorCodes.NOT_FOUND)
        if e.error_code == errors.RepositoryErrorCodes.USER_INVALID_DATA:
            raise errors.BadRequestError(errors.ServiceErrorCodes.BAD_REQUEST)
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    except Exception as e:
        # handle other errors
        _logger.error("error updating user by id", err_msg=str(e))
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    _logger.info("User updated")
    return response


def delete_user_by_id(user_id: str) -> bool:
    _logger.info("Deleting user by id...")
    try:
        user_repository.delete_user_by_id(user_id)
    except errors.RepositoryError as e:
        # handle repository errors
        _logger.error("error deleting user by id", err_msg=str(e))
        if e.error_code == errors.RepositoryErrorCodes.USER_NOT_FOUND:
            raise errors.NotFoundError(errors.ServiceErrorCodes.NOT_FOUND)
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    except Exception as e:
        # handle other errors
        _logger.error("error deleting user by id", err_msg=str(e))
        raise errors.InternalServerError(errors.ServiceErrorCodes.INTERNAL_SERVER_ERROR)
    _logger.info("User deleted")
    return True