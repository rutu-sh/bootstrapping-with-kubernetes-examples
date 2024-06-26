import os


SERVICE_NAME = os.getenv("SERVICE_NAME", "simple-restapi-server")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", "8000")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_TIME_FORMAT = f"%Y-%m-%d %H:%M:%S"
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_TABLE_USERS = os.getenv("DB_TABLE_USERS")

BIND_PARAMS = {
    "service_name": SERVICE_NAME,
}
