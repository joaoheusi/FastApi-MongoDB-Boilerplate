from fastapi import Body, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from src.modules.users.models.documents import User
from src.modules.users.models.schemas import CreateUser
from src.modules.users.usecases.create_user import create_user_usecase

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=User)
async def create_user(requestBody: CreateUser = Body(...)):
    user: User = await create_user_usecase(requestBody)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)
