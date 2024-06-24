from fastapi.routing import APIRouter

router = APIRouter(prefix="/rest/v1/users", tags=["users"])

@router.get("/")
async def get_users():
    return {"message": "get_users"}


@router.post("/")
async def create_user():
    return {"message": "created user"}


