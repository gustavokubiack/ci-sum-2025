from app import sum_f
import pytest


@pytest.mark.parametrize(
    "v1, v2, expected", [
        (1, 2, 3), 
        (2, 4, 6),
        (7, 3, 10),
    ]
)
def test_sum_f(v1, v2, expected):
    assert sum_f(v1, v2) == expected
