from typing import List

from beanie import Document
from pydantic import EmailStr
from pydantic.fields import Field
from src.shared.utils.uuid import uuid4_gen


class User(Document):
    id: str = Field(default_factory=uuid4_gen, alias="_id")
    username: str
    email: EmailStr
    password: str
    firstName: str
    lastName: str
    isActive: bool = True
    allowedModules: List[str] = ["users"]

    class Collection:
        name = "users"

    class Settings:
        use_state_management = True
