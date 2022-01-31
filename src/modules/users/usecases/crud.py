from typing import List

from fastapi import HTTPException, status
from src.modules.users.models.documents import User
from src.modules.users.models.schemas import CreateUser, UpdateUserInfo, UserInfo
from src.shared.utils.encryption import encrypt


async def create_user_usecase(create_user: CreateUser) -> UserInfo:
    new_user = User(
        username=create_user.username,
        email=create_user.email,
        password=encrypt(create_user.password),
        firstName=create_user.firstName,
        lastName=create_user.lastName,
    )
    db_response: User = await new_user.insert()
    created_user = await User.find_one(User.id == db_response.id).project(UserInfo)
    return created_user


async def find_all_usecase(skip: int, limit: int) -> List[UserInfo]:
    users = await User.find().project(UserInfo).skip(skip).limit(limit).to_list()
    if users:
        return users
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Could not find any users.",
    )


async def find_one_by_id_usecase(id: str) -> UserInfo:
    user = await User.find_one(User.id == id).project(UserInfo)
    if user:
        return user
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        detail="User with given ID not found.",
    )


async def change_user_info_usecase(id: str, new_user_info: UpdateUserInfo) -> UserInfo:
    user = await User.find_one(User.id == id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with given ID not found.",
        )
    if new_user_info.lastName:
        user.lastName = new_user_info.lastName
    if new_user_info.firstName:
        user.firstName = new_user_info.firstName
    await user.save_changes()
    user_new_value = await User.find_one(User.id == id).project(UserInfo)
    return user_new_value


async def delete_user_usecase(id: str) -> None:
    user = await User.find_one(User.id == id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with given ID not found.",
        )
    await user.delete()
    return None
