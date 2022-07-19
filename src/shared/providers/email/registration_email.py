from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi_mail import MessageSchema
from src.shared.providers.email.config import fast_mail
from src.shared.providers.email.schemas.send_registration_email_props import (
    SendRegistrationEmailProps,
)


async def send_registration_email(props: SendRegistrationEmailProps):
    try:
        body_content = {
            "firstName": props.user.firstName,
            "url": props.validationUrl,
        }
        message = MessageSchema(
            subject="Confirm your email",
            recipients=[props.user.email],
            template_body=body_content,
            subtype="html",
        )
        await fast_mail.send_message(message, template_name="registration_email.html")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"detail": "Could not send registration email."},
        )
