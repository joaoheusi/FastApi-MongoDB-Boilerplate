from httpx import Client
from tests.utils import (
    TestInfo,
    get_test_successful_message,
    get_test_unsuccessful_message,
)

delete_user_info = TestInfo(
    module="users",
    test_name="delete_user",
    route="/users/<id>",
    method="DELETE",
)


def test_delete_user(client: Client, user_id: str):
    try:
        assert user_id is not False, "Didn't receive a valid id"
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 204, "Did not delete user."
        print(get_test_successful_message(delete_user_info))
    except AssertionError as assertion_error:
        print(get_test_unsuccessful_message(delete_user_info, error=assertion_error))
        return False
