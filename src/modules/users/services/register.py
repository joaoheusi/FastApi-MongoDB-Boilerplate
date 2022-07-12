from typing import Tuple

from fastapi import BackgroundTasks, HTTPException, status
from src.modules.users.models.documents import User
from src.modules.users.models.schemas import CreateUser, UserInfo
from src.modules.users.services.config import API_URL
from src.shared.providers.email.registration_email import send_registration_email
from src.shared.providers.email.schemas.send_registration_email_props import (
    SendRegistrationEmailProps,
)
from src.shared.utils.encryption import encrypt, encrypt_uuid


async def register_user_service(
    create_user: CreateUser,
) -> Tuple[UserInfo, BackgroundTasks]:

    email_used = await User.find_one(User.email == create_user.email)
    if not email_used:

        new_user = User(
            username=create_user.username,
            email=create_user.email,
            password=encrypt(create_user.password),
            firstName=create_user.firstName,
            lastName=create_user.lastName,
        )
        db_response: User = await new_user.insert()
        created_user = await User.find_one(User.id == db_response.id).project(UserInfo)

        enc_uuid = encrypt_uuid(db_response.id)
        print(API_URL)
        url = API_URL + "/users/validate_email/{}".format(enc_uuid)
        props = SendRegistrationEmailProps(user=created_user, validationUrl=url)

        background_tasks = BackgroundTasks()
        background_tasks.add_task(send_registration_email, props)

        return (created_user, background_tasks)

    # If email already in use raise error
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail={"error": "User with provided e-mail already exists"},
    )
