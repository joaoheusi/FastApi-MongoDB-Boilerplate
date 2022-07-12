from httpx import Client
from tests.utils import (
    TestInfo,
    get_test_successful_message,
    get_test_unsuccessful_message,
)

find_user_by_id_info = TestInfo(
    module="users",
    test_name="find_user_by_id",
    route="/users/<id>",
    method="GET",
)


def test_find_user_by_id(client: Client, id: str):
    try:
        assert id is not False, "Didn't receive a valid id"
        response = client.get(f"/users/{id}")
        assert response.status_code == 200, "Did not find user."
        assert response.json() != {}, "Did not find user."
        print(get_test_successful_message(find_user_by_id_info))
    except AssertionError as assertion_error:
        print(
            get_test_unsuccessful_message(find_user_by_id_info, error=assertion_error)
        )
