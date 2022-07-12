from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from src.modules.users.models.schemas import CreateUser
from tests.utils import TestInfo, get_test_successful_message

test_info = TestInfo(
    module="users",
    test_name="create_user",
    route="/users",
    method="POST",
)


def test_create_user(client: TestClient, data: CreateUser):
    body = jsonable_encoder(data)
    response = client.post("/users", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "username": data.username,
        "email": data.email,
        "firstName": data.firstName,
        "lastName": data.lastName,
    }
    print(get_test_successful_message(test_info))
