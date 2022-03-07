from typing import List

from fastapi import Body, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from src.auth.bearer import JWTBearer
from src.modules.users.models.schemas import CreateUser, UpdateUserInfo, UserInfo
from src.modules.users.services.crud import (
    change_user_info_service,
    create_user_service,
    delete_user_service,
    find_all_service,
    find_one_by_id_service,
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[
        Depends(
            JWTBearer(
                tokenUrl="auth",
                module_name="users",
            )
        ),
    ],
)


@router.post("", response_model=UserInfo)
async def create_user(requestBody: CreateUser = Body(...)):
    user: UserInfo = await create_user_service(requestBody)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)


@router.get("", response_model=List[UserInfo])
async def find_users(skip: int = 0, limit: int = 0):
    users = await find_all_service(skip=skip, limit=limit)
    return JSONResponse(jsonable_encoder(users), status_code=status.HTTP_200_OK)


@router.get("/{id}", response_model=UserInfo)
async def find_user_by_id(id: str):
    user = await find_one_by_id_service(id)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)


@router.patch("/{id}", response_model=UserInfo)
async def edit_user(id: str, requestBody: UpdateUserInfo = Body(...)):
    user = await change_user_info_service(id, requestBody)
    return JSONResponse(user.dict(), status_code=status.HTTP_200_OK)


@router.delete("/{id}")
async def delete_user(id: str):
    await delete_user_service(id)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
