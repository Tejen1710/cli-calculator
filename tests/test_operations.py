import math
import pytest
from calculator.operations import add, sub, mul, div

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (1, 2, 3),
        (-1, 5, 4),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (5, 2, 3),
        (-1, -1, 0),
        (2.5, 0.5, 2.0),
    ],
)
def test_sub(a, b, expected):
    assert sub(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (3, 2, 6),
        (-1, 5, -5),
        (2.5, 0.5, 1.25),
    ],
)
def test_mul(a, b, expected):
    assert mul(a, b) == expected


def test_div_basic():
    assert div(10, 2) == 5


def test_div_float_precision():
    assert math.isclose(div(1, 4), 0.25)


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)