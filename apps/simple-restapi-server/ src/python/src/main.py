# standard libraries


# installed libraries
import uvicorn
from fastapi import FastAPI

# custom imports
from controller import controller
from common import common, config

_logger = common.get_logger(
    __name__, 
    bind_params=config.BIND_PARAMS.update({
        "param1": "value1",
        "param2": "value2"
    }), 
    handlers=[
        common.StreamHandler, 
        # common.FileHandler
    ]
)

def main():
    app = FastAPI()
    app.include_router(controller.router)
    _logger.info("Starting the server")
    uvicorn.run(app, host=config.HOST, port=int(config.PORT))


if __name__ == '__main__':
    main() 