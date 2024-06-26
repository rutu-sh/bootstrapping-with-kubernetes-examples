# standard libraries 
from typing import List
from datetime import datetime

# installed libraries

# custom libraries
from models import models
from common import common, config
from repository import db_common


_logger = common.get_logger("repository.users")


def create_user(user: models.User) -> models.UserDB:
    _logger.info("Creating user...")
    cnx = db_common.get_connection()
    try:
        query = """
                INSERT INTO users (id, name, email, age, created_at, updated_at)
                VALUES (%(id)s, %(name)s, %(email)s, %(age)s, %(created_at)s, %(updated_at)s)
            """
        _logger.info("Creating user", query=query, user=user.model_dump())
        dt = datetime.now().strftime(config.DATETIME_FORMAT)
        user_db = models.UserDB(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            created_at=dt,
            updated_at=dt
        )
        db_common.write(cnx, query, user_db.model_dump())
        _logger.info("User created")
        return user
    except Exception as e:
        _logger.error("Error creating user", exc_info=True)
        raise
    finally:
        _logger.info("Closing connection")
        db_common.close_connection(cnx)


def get_users() -> List[models.UserDB]:
    _logger.info("Getting users...")
    try:
        cnx = db_common.get_connection()
        query = f"""
            SELECT * FROM {config.DB_TABLE_USERS}
        """
        results = db_common.read(cnx, query)
    except Exception as e:
        _logger.error("Error getting users", exc_info=True)
        raise
    finally:
        _logger.info("Closing connection")
        db_common.close_connection(cnx)
    users = [models.UserDB(**result) for result in results]
    _logger.info("Got users")
    return users


def get_user_by_id(user_id: str) -> models.UserDB:
    _logger.info("Getting user by id...")
    try:
        cnx = db_common.get_connection()
        query = f"""
            SELECT * FROM {config.DB_TABLE_USERS} WHERE id = %(id)s
        """
        params = {"id": user_id}
        results = db_common.read(cnx, query, params)
        return models.UserDB(**results[0])
    except Exception as e:
        _logger.error("Error getting user by id", exc_info=True)
        raise
    finally:
        _logger.info("Closing connection")
        db_common.close_connection(cnx)

def update_user_by_id(user_id: str, user: models.UserDB) -> models.UserDB:
    _logger.info("Updating user by id...")
    try:
        cnx = db_common.get_connection()
        query = f"""
            UPDATE {config.DB_TABLE_USERS}
            SET name = %(name)s, email = %(email)s, age = %(age)s, updated_at = %(updated_at)s
            WHERE id = %(id)s
        """
        params = {
            "id": user_id,
            "name": user.name,
            "email": user.email,
            "age": user.age,
            "updated_at": datetime.now().strftime(config.DATETIME_FORMAT)
        }
        db_common.write(cnx, query, params)
        return user
    except Exception as e:
        _logger.error("Error updating user by id", exc_info=True)
        raise
    finally:
        _logger.info("Closing connection")
        db_common.close_connection(cnx)