from fastapi import status
from fastapi.exceptions import HTTPException
from src.modules.users.models.documents import User
from src.shared.utils.encryption import decrypt_uuid


async def validate_email_service(token: str):
    try:
        dec_uuid = decrypt_uuid(token)
        user = await User.find_one(User.id == dec_uuid)
        if user:

            if user.isEmailConfirmed is True:
                # raise error if email is already confirmed
                raise_validate_email_service_error(1)

            user.isEmailConfirmed = True
            await user.save_changes()
            return

        # raise error if there is no user with given uuid
        raise_validate_email_service_error()

    except Exception:
        print(Exception)
        raise_validate_email_service_error()


def raise_validate_email_service_error(code: int = None):
    """
    Service errors.
    """
    if code == 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"detail": "User already validated."},
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"detail": "Invalid token."},
        )
