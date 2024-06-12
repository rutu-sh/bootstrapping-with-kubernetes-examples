from controller import controller
from common import common

_logger = common.get_logger("test", bind_params={"param1": "value1", "param2": "value2"}, handlers=[common.logging.StreamHandler(), common.logging.FileHandler("log.txt")])

def main():
    _logger.error("Starting the server", a=1, b=3)
    _logger.warning("Starting the server")
    _logger.debug("Starting the server")
    _logger.info("Starting the server")
    _logger.info("Server started")


if __name__ == '__main__':
    main() 