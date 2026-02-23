import pytest


def test_user_fixture(user):
    assert user == {"id": 1, "name": "bob"}
