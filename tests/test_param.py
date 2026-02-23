import pytest


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (-1, 1, 0), (0, 0, 0), (2, 3, 5)])
def test_add_param(a, b, expected):
    assert a + b == expected
