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
async def get_users() -> list[models.UserResponse]:
    _logger.info("Getting users...")
    users = user_service.get_users()
    return users

@router.post("/")
async def create_user(user: models.UserRequest) -> models.UserResponse:
    _logger.info("Creating user...")
    user = user_service.create_user(user)
    return user

@router.get("/{user_id}")
async def get_user_by_id(user_id: str) -> models.UserResponse:
    _logger.info("Getting user by id...")
    user = user_service.get_user_by_id(user_id)
    return user

@router.put("/{user_id}")
async def update_user(user_id: str, user: models.UserRequest) -> models.UserResponse:
    _logger.info("Updating user...")
    user = user_service.update_user_by_id(user_id, user)
    return user