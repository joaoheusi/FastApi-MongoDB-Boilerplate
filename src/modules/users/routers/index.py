from typing import List

from fastapi import Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from src.modules.users.models.schemas import CreateUser, UpdateUserInfo, UserInfo
from src.modules.users.usecases.crud import (
    change_user_info_usecase,
    create_user_usecase,
    delete_user_usecase,
    find_all_usecase,
    find_one_by_id_usecase,
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("", response_model=UserInfo)
async def create_user(requestBody: CreateUser = Body(...)):
    user: UserInfo = await create_user_usecase(requestBody)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)


@router.get("", response_model=List[UserInfo])
async def find_users(skip: int = 0, limit: int = 0):
    users = await find_all_usecase(skip=skip, limit=limit)
    return JSONResponse(jsonable_encoder(users), status_code=status.HTTP_200_OK)


@router.get("/{id}", response_model=UserInfo)
async def find_user_by_id(id: str):
    user = await find_one_by_id_usecase(id)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)


@router.patch("/{id}", response_model=UserInfo)
async def edit_user(id: str, requestBody: UpdateUserInfo = Body(...)):
    user = await change_user_info_usecase(id, requestBody)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)


@router.delete("/{id}")
async def delete_user(id: str):
    await delete_user_usecase(id)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
