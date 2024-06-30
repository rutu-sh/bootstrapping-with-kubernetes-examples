# standard libraries
from typing import List

# installed libraries
import mysql.connector

# custom libraries
from common import common, config
from models import errors


_logger = common.get_logger("repository.mysql_common")


def get_connection(database: str = config.DB_NAME) -> mysql.connector.MySQLConnection:
    _logger.info(f"connecting to database: {database}")
    try:
        cnx = mysql.connector.connect(
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            database=database
        )
        _logger.info(f"connected to database: {database}")
        return cnx
    except mysql.connector.Error as err:
        _logger.error(f"error connecting to database: {database}", exc_info=True)
        raise errors.DatabaseError(errors.RepositoryErrorCodes.DATABASE_CONNECTION_CREATE_FAILED)
    except Exception as e:
        _logger.error(f"error connecting to database: {database}", exc_info=True)
        raise errors.DatabaseError(errors.RepositoryErrorCodes.DATABASE_CONNECTION_CREATE_FAILED) 


def close_connection(cnx) -> bool:
    _logger.info("closing database connection")
    try:
        cnx.close()
        _logger.info("closed database connection")
        return True
    except mysql.connector.Error as err:
        _logger.error("error closing database connection", exc_info=True)
        raise errors.DatabaseError(errors.RepositoryErrorCodes.DATABASE_CONNECTION_CLOSE_FAILED)
    


def read(cnx: mysql.connector.MySQLConnection, query: str, params: dict = None) -> List[dict]:
    _logger.info(f"executing query...")
    cursor = cnx.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        _logger.info(f"finished executing query. Returning results...")
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        _logger.error(f"error executing query.", exc_info=True)
        raise errors.DatabaseError(errors.RepositoryErrorCodes.DATABASE_READ_FAILED)
    finally:
        _logger.info("closing cursor")
        cursor.close() 


def write(cnx: mysql.connector.MySQLConnection, query: str, params: dict = None) -> bool:
    _logger.info(f"executing query...")
    cursor = cnx.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        cnx.commit()
        _logger.info(f"finished executing query.")
        return True
    except mysql.connector.Error as err:
        _logger.error(f"error executing query.", exc_info=True)
        raise errors.DatabaseError(errors.RepositoryErrorCodes.DATABASE_WRITE_FAILED)
    finally:
        _logger.info("closing cursor")
        cursor.close()