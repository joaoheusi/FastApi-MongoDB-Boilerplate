from pydantic import BaseModel
from src.modules.users.models.schemas import UserInfo


class SendRegistrationEmailProps(BaseModel):
    user: UserInfo
    validationUrl: str
