# standard libraries 
from typing import List

# installed libraries

# custom libraries
from models import models
from common import common, config
from repository import db_common


_logger = common.get_logger("repository.users")


def create_user(user: models.UserDB) -> models.UserDB:
    _logger.info("Creating user...")
    cnx = db_common.get_connection()
    cursor = cnx.cursor(dictionary=True)
    try:
        query = """
            INSERT INTO users (name, email, age, created_at, updated_at)
            VALUES (%(name)s, %(email)s, %(age)s, %(created_at)s, %(updated_at)s)
        """
        cursor.execute(query, user.to_dict(deep=True))
        cnx.commit()
        _logger.info("User created")
        return user
    except Exception as e:
        _logger.error("Error creating user", exc_info=True)
        raise
    finally:
        _logger.info("Closing cursor")
        cursor.close()
        _logger.info("Closing connection")
        db_common.close_connection(cnx)


def get_users() -> List[models.UserDB]:
    _logger.info("Getting users...")
    cnx = db_common.get_connection()
    query = f"""
        SELECT * FROM {config.DB_TABLE_USERS}
    """
    results = db_common.read(cnx, query)
    users = [models.UserDB(**result) for result in results]
    _logger.info("Got users")
    return users

