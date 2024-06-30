# standard libraries
from typing import List

# installed libraries
from starlette.responses import JSONResponse
from fastapi.routing import APIRouter

# custom libraries
from models import models, errors
from service import user_service
from common import common

_logger = common.get_logger("controller.users")
router = APIRouter(prefix="/rest/v1/users", tags=["users"])


def _handle_service_error(e: errors.ServiceError) -> JSONResponse:
    if e.error_code == errors.ServiceErrorCodes.NOT_FOUND:
        return JSONResponse(status_code=404, content={"error": "not found"})
    elif e.error_code == errors.ServiceErrorCodes.BAD_REQUEST:
        return JSONResponse(status_code=400, content={"error": "bad request"})
    return JSONResponse(status_code=500, content={"error": "internal server error"})


@router.get("/")
async def get_users() -> list[models.UserResponse]:
    _logger.info("Getting users...")
    try:
        users = user_service.get_users()
    except errors.ServiceError as e:
        # handle service errors
        _logger.error("error getting users", err_msg=str(e))
        return _handle_service_error(e)
    return users

@router.post("/")
async def create_user(user: models.UserRequest) -> models.UserResponse:
    _logger.info("Creating user...")
    try:
        user = user_service.create_user(user)
    except errors.ServiceError as e:
        # handle service errors
        _logger.error("error creating user", err_msg=str(e))
        return _handle_service_error(e)
    return user

@router.get("/{user_id}")
async def get_user_by_id(user_id: str) -> models.UserResponse:
    _logger.info("Getting user by id...")
    try:
        user = user_service.get_user_by_id(user_id)
    except errors.ServiceError as e:
        # handle service errors
        _logger.error("error getting user by id", err_msg=str(e))
        return _handle_service_error(e)
    return user

@router.put("/{user_id}")
async def update_user(user_id: str, user: models.UserRequest) -> models.UserResponse:
    _logger.info("Updating user...")
    try:
        user = user_service.update_user_by_id(user_id, user)
    except errors.ServiceError as e:
        # handle service errors
        _logger.error("error updating user", err_msg=str(e))
        return _handle_service_error(e)
    return user