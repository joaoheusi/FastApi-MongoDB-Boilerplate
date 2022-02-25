from typing import Optional

from pydantic import BaseModel, EmailStr, StrictStr


class UserInfo(BaseModel):
    username: str
    email: EmailStr
    firstName: StrictStr
    lastName: StrictStr


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    firstName: StrictStr
    lastName: StrictStr


class UpdateUserInfo(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]


class UpdateUserEmail(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]


class UpdateUserPassword(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
