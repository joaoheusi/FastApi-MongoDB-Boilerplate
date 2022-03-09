from typing import Tuple

from fastapi import BackgroundTasks
from src.modules.users.models.documents import User
from src.modules.users.models.schemas import CreateUser, UserInfo
from src.shared.providers.email.registration_email import send_registration_email
from src.shared.utils.encryption import encrypt


async def register_user_service(
    create_user: CreateUser,
) -> Tuple[UserInfo, BackgroundTasks]:
    new_user = User(
        username=create_user.username,
        email=create_user.email,
        password=encrypt(create_user.password),
        firstName=create_user.firstName,
        lastName=create_user.lastName,
    )
    db_response: User = await new_user.insert()
    created_user = await User.find_one(User.id == db_response.id).project(UserInfo)
    background_tasks = BackgroundTasks()
    background_tasks.add_task(send_registration_email, created_user)
    return (created_user, background_tasks)
