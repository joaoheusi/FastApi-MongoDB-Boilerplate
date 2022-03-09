from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi_mail import MessageSchema
from src.modules.users.models.schemas import UserInfo
from src.shared.providers.email.config import fast_mail


async def send_registration_email(user: UserInfo):
    try:
        body_content = {"firstName": user.firstName}
        message = MessageSchema(
            subject="Confirm your email",
            recipients=[user.email],
            template_body=body_content,
            subtype="html",
        )
        await fast_mail.send_message(message, template_name="registration_email.html")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"detail": "Could not send registration email."},
        )
