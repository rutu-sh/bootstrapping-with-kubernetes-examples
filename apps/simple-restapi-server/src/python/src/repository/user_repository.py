# standard libraries 
from typing import List
from datetime import datetime

# installed libraries

# custom libraries
from models import models, errors
from common import common, config
from repository import db_common


_logger = common.get_logger("repository.users")


def _is_user_exists(cnx, user_id: str) -> bool:
    _logger.info("checking if user exists...")
    try:
        query = f"""
            SELECT id FROM {config.DB_TABLE_USERS} WHERE id = %(id)s
        """
        params = {"id": user_id}
        results = db_common.read(cnx, query, params)
        return len(results) > 0
    except Exception as e:
        _logger.error("error checking if user exists", exc_info=True)
        raise errors.DatabaseError(errors.RepositoryErrorCodes.DATABASE_READ_FAILED)
    

def _convert_user_record_to_user_db(user: dict) -> models.UserDB:
    try:
        user_db = models.UserDB(**user)
        return user_db
    except Exception as e:
        _logger.error("error converting user record to user db", exc_info=True)
        raise errors.UserError(errors.RepositoryErrorCodes.USER_INVALID_RECORD)



def create_user(user: models.User) -> models.UserDB:
    _logger.info("creating user...")
    cnx = db_common.get_connection()
    try:
        query = """
                INSERT INTO users (id, name, email, age, created_at, updated_at)
                VALUES (%(id)s, %(name)s, %(email)s, %(age)s, %(created_at)s, %(updated_at)s)
            """
        _logger.info("creating user", query=query, user=user.model_dump())
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
        _logger.info("user created")
        return user_db
    except errors.RepositoryError as e:
        raise
    except Exception as e:
        _logger.error("error creating user", exc_info=True)
        raise errors.UserError(errors.RepositoryErrorCodes.USER_INVALID_DATA)
    finally:
        _logger.info("closing connection")
        db_common.close_connection(cnx)


def get_users() -> List[models.UserDB]:
    _logger.info("fetching users...")
    try:
        cnx = db_common.get_connection()
        query = f"""
            SELECT * FROM {config.DB_TABLE_USERS}
        """
        results = db_common.read(cnx, query)
    except Exception as e:
        _logger.error("error fetching users", exc_info=True)
        raise
    finally:
        _logger.info("closing connection")
        db_common.close_connection(cnx) 
    
    users = [_convert_user_record_to_user_db(user) for user in results]
    _logger.info("fetched users")
    return users


def get_user_by_id(user_id: str) -> models.UserDB:
    _logger.info("getting user by id...")
    try:
        cnx = db_common.get_connection()
        query = f"""
            SELECT * FROM {config.DB_TABLE_USERS} WHERE id = %(id)s
        """
        params = {"id": user_id}
        results = db_common.read(cnx, query, params)
        if len(results) == 0:
            raise errors.UserError(errors.RepositoryErrorCodes.USER_NOT_FOUND)
        
        return _convert_user_record_to_user_db(results[0])
    except Exception as e:
        _logger.error("error getting user by id", exc_info=True)
        raise
    finally:
        _logger.info("closing connection")
        db_common.close_connection(cnx)


def update_user_by_id(user_id: str, user: models.User) -> models.UserDB:
    _logger.info("updating user by id...")
    try:
        cnx = db_common.get_connection()
        if not _is_user_exists(cnx, user_id):
            raise errors.UserError(errors.RepositoryErrorCodes.USER_NOT_FOUND)

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
        _logger.error("error updating user by id", exc_info=True)
        raise
    finally:
        _logger.info("closing connection")
        db_common.close_connection(cnx)


def delete_user_by_id(user_id: str) -> bool:
    _logger.info("deleting user by id...")
    try:
        cnx = db_common.get_connection()
        if not _is_user_exists(cnx, user_id):
            raise errors.UserError(errors.RepositoryErrorCodes.USER_NOT_FOUND)

        query = f"""
            DELETE FROM {config.DB_TABLE_USERS} WHERE id = %(id)s
        """
        params = {"id": user_id}
        db_common.write(cnx, query, params)
        return True
    except errors.RepositoryError as e:
        raise
    except Exception as e:
        _logger.error("error deleting user by id", exc_info=True)
        raise errors.RepositoryError(errors.RepositoryErrorCodes.GENERIC_REPOSITORY_ERROR)
    finally:
        _logger.info("closing connection")
        db_common.close_connection(cnx)
