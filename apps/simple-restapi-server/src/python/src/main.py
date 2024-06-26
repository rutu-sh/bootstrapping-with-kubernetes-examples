# standard libraries


# installed libraries
import uvicorn
from fastapi import FastAPI

# custom imports
from controller import user_controller, health_check_controller
from common import common, config

_logger = common.get_logger(
    __name__, 
    bind_params=config.BIND_PARAMS, 
    handlers=[
        common.StreamHandler, 
        # common.FileHandler
    ]
)

def main():
    app = FastAPI()
    app.include_router(health_check_controller.router)
    app.include_router(user_controller.router)
    _logger.info("Starting the server")
    uvicorn.run(app, host=config.HOST, port=int(config.PORT))


if __name__ == '__main__':
    main() 