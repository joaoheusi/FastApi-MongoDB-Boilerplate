from fastapi.encoders import jsonable_encoder
from httpx import Client
from src.modules.users.models.schemas import UpdateUserInfo
from tests.utils import (
    TestInfo,
    get_test_successful_message,
    get_test_unsuccessful_message,
)

edit_user_info = TestInfo(
    module="users",
    test_name="edit_user",
    route="/users/<id>",
    method="PATCH",
)


def test_edit_user(client: Client, user_id: str, edit_data: UpdateUserInfo):
    try:
        body = jsonable_encoder(edit_data.dict())
        response = client.patch(f"/users/{user_id}", json=body)
        assert response.status_code == 200, "Did not edit user."
        assert (
            response.json()["firstName"] == edit_data.firstName
        ), "firstName does not match giver firstName"
        assert (
            response.json()["lastName"] == edit_data.lastName
        ), "lastName does not match giver lastName"
        print(get_test_successful_message(edit_user_info))
        return response.json()["id"]
    except AssertionError as assertion_error:
        print(get_test_unsuccessful_message(edit_user_info, error=assertion_error))
        return False
