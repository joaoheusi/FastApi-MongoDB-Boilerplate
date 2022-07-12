from fastapi.testclient import TestClient

from app import app
from src.modules.users.models.schemas import CreateUser
from tests.modules.users._create_user import test_create_user


def main():
    user_data = CreateUser(
        username="test_user",
        email="test@email.com",
        password="password",
        firstName="Test",
        lastName="User",
    )
    with TestClient(app) as client:
        test_create_user(client, user_data)


if __name__ == "__main__":
    main()
