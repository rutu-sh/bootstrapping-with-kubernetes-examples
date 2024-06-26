# standard libraries
from typing import List

# installed libraries
from starlette.responses import JSONResponse
from fastapi.routing import APIRouter

# custom libraries
from models import models
from service import user_service
from common import common

_logger = common.get_logger("controller.users")
router = APIRouter(prefix="/rest/v1/users", tags=["users"])

@router.get("/")
async def get_users() -> list[models.User]:
    _logger.info("Getting users...")
    users = user_service.get_users()
    return users



@router.post("/")
async def create_user():
    return {"message": "created user"}


