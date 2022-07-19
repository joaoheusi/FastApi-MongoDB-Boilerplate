from httpx import Client

from app import app
from src.modules.users.models.schemas import CreateUser, UpdateUserInfo
from tests.modules.users.test_create_user import (
    test_create_duplicate_user,
    test_create_user,
)
from tests.modules.users.test_delete_user import test_delete_user
from tests.modules.users.test_edit_user import test_edit_user
from tests.modules.users.test_find_user_by_id import test_find_user_by_id
from tests.modules.users.test_find_users import test_find_users


def main():
    user_data = CreateUser(
        username="test_user",
        email="test@email.com",
        password="password",
        firstName="Test",
        lastName="User",
    )

    edit_data = UpdateUserInfo(
        firstName="Test",
        lastName="User",
    )

    with Client(base_url="http://localhost:8000") as client:
        created_id = test_create_user(client, user_data)
        test_create_duplicate_user(client, user_data)
        test_find_users(client)
        test_find_user_by_id(client, created_id)
        test_edit_user(client, created_id, edit_data=edit_data)
        # test_delete_user(client, created_id)


if __name__ == "__main__":
    main()
