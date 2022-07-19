from app import app
from httpx import Client
from tests.utils import (
    TestInfo,
    get_test_successful_message,
    get_test_unsuccessful_message,
)

find_users_info = TestInfo(
    module="users",
    test_name="find_users",
    route="/users",
    method="GET",
)


def test_find_users(client: Client):
    try:
        response = client.get("/users")
        assert response.status_code == 200, "Did not find any users."
        assert response.json() != [], "Did not find any users."
        print(get_test_successful_message(find_users_info))
    except AssertionError as assertion_error:
        print(get_test_unsuccessful_message(find_users_info, error=assertion_error))
