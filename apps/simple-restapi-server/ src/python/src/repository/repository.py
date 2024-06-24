# standard libraries 

# installed libraries
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# custom libraries
from common import common, config
from models import models


_logger = common.get_logger(__name__)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{config.DB_HOST}/{config.DB_NAME}"


def configure_db_engine() -> sqlalchemy.Engine:
    """
    Configures and returns a SQLAlchemy engine
    """
    _logger.info("Configuring the database engine")
    return create_engine(SQLALCHEMY_DATABASE_URL)
