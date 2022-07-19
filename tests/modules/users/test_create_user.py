from app import app
from fastapi.encoders import jsonable_encoder
from httpx import Client
from src.modules.users.models.schemas import CreateUser
from tests.utils import (
    TestInfo,
    get_test_successful_message,
    get_test_unsuccessful_message,
)

create_user_info = TestInfo(
    module="users",
    test_name="create_user",
    route="/users",
    method="POST",
)

create_duplicate_user_info = TestInfo(
    module="users",
    test_name="create_duplicate_user",
    route="/users",
    method="POST",
)


def test_create_user(client: Client, user_data: CreateUser):
    try:
        body = jsonable_encoder(user_data.dict())
        response = client.post("/users", json=body)
        assert response.status_code == 200, "Did not create User."
        assert (
            response.json()["username"] == user_data.username
        ), "username does not match giver username"
        assert (
            response.json()["email"] == user_data.email
        ), "email does not match giver email"
        assert (
            response.json()["firstName"] == user_data.firstName
        ), "firstName does not match giver firstName"
        assert (
            response.json()["lastName"] == user_data.lastName
        ), "lastName does not match giver lastName"
        print(get_test_successful_message(create_user_info))
        return response.json()["id"]

    except AssertionError as assertion_error:
        print(get_test_unsuccessful_message(create_user_info, error=assertion_error))
        return False


def test_create_duplicate_user(client: Client, user_data: CreateUser):
    try:
        body = jsonable_encoder(user_data.dict())
        response = client.post("/users", json=body)
        assert (
            response.status_code == 409
        ), "Did not raise conflict with duplicate email"
        assert response.json()["detail"] == {
            "error": "User with provided e-mail already exists"
        }, "Did not raise conflict with duplicate email"
        print(get_test_successful_message(create_duplicate_user_info))
    except AssertionError as assertion_error:
        print(
            get_test_unsuccessful_message(
                create_duplicate_user_info, error=assertion_error
            )
        )
