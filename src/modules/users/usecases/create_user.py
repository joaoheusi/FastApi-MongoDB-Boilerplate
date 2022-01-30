from src.modules.users.models.documents import User
from src.modules.users.models.schemas import CreateUser, UserInfo
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
