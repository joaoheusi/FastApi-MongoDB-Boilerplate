from fastapi.testclient import TestClient
from httpx import Client

from app import app
from src.modules.users.models.schemas import CreateUser
from tests.modules.users.test_create_user import (
    test_create_duplicate_user,
    test_create_user,
)


def main():
    user_data = CreateUser(
        username="test_user",
        email="test@email.com",
        password="password",
        firstName="Test",
        lastName="User",
    )

    with Client(base_url="http://localhost:8000") as client:
        test_create_user(client, user_data)
        test_create_duplicate_user(client, user_data)


if __name__ == "__main__":
    main()
