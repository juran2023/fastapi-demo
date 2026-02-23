from unittest.mock import patch
import time


def now():
    return time.time()


def test_now_mocked():
    with patch("time.time", return_value=1234567890):
        assert now() == 1234567890
