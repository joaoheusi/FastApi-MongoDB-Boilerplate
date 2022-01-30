from typing import List

from fastapi import Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from src.modules.users.models.documents import User
from src.modules.users.models.schemas import CreateUser, UserInfo
from src.modules.users.usecases.create_user import create_user_usecase

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("", response_model=User)
async def create_user(requestBody: CreateUser = Body(...)):
    user: UserInfo = await create_user_usecase(requestBody)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)


@router.get("", response_model=List[UserInfo])
async def find_users(skip=0, limit=0):
    users = await User.find().project(UserInfo).skip(skip).limit(limit).to_list()
    return JSONResponse(jsonable_encoder(users), status_code=status.HTTP_200_OK)


@router.get("/{id}", response_model=UserInfo)
async def find_user_by_id(id: str):
    user = await User.find_one(User.id == id).project(UserInfo)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)
