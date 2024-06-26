# standard libraries
from typing import List

# installed libraries
import mysql.connector

# custom libraries
from common import common, config


_logger = common.get_logger("repository.mysql_common")


def get_connection(database: str = config.DB_NAME) -> mysql.connector.MySQLConnection:
    _logger.info(f"Connecting to database: {database}")
    try:
        cnx = mysql.connector.connect(
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            database=database
        )
        _logger.info(f"Connected to database: {database}")
        return cnx
    except mysql.connector.Error as err:
        _logger.error(f"Error connecting to database: {database}", exc_info=True)
    except Exception as e:
        _logger.error(f"Error connecting to database: {database}", exc_info=True)
    
    return None
    


def close_connection(cnx) -> bool:
    _logger.info("Closing database connection", database=cnx.database)
    try:
        cnx.close()
        _logger.info("Closed database connection")
        return True
    except mysql.connector.Error as err:
        _logger.error("Error closing database connection", exc_info=True)
        raise
    


def query(cnx: mysql.connector.MySQLConnection, query: str, params: dict = None) -> List[dict]:

    _logger.info(f"Executing query...")
    cursor = cnx.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        _logger.info(f"Finished executing query. Returning results...")
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        _logger.error(f"Error executing query.", exc_info=True)
        raise
    finally:
        _logger.info("Closing cursor")
        cursor.close()

    