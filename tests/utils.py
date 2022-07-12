from pydantic import BaseModel


class TestInfo(BaseModel):
    module: str
    test_name: str
    route: str
    method: str


def get_test_successful_message(test_info: TestInfo) -> str:
    return f"|{test_info.module}|{test_info.test_name} passed."
