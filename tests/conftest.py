import pytest


@pytest.fixture
def user():
    return {"id": 1, "name": "bob"}
