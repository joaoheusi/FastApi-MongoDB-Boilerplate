from typing import Optional

from pydantic import BaseModel, EmailStr


class UserInfo(BaseModel):
    username: str
    email: EmailStr
    firstName: str
    lastName: str


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    firstName: str
    lastName: str


class UpdateUserInfo(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]


class UpdateUserEmail(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]


class UpdateUserPassword(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
