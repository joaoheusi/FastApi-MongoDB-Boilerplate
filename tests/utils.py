from pydantic import BaseModel


class TestInfo(BaseModel):
    module: str
    test_name: str
    route: str
    method: str


def get_test_successful_message(test_info: TestInfo) -> str:
    return f"|PASS| {test_info.module} | {test_info.test_name} passed."


def get_test_unsuccessful_message(test_info: TestInfo, error: Exception) -> str:
    return f"|FAIL| {test_info.module} | {test_info.test_name}  did not pass. \
     Assertion Error: {error}"
