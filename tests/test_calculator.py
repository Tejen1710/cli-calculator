from calculator.calculator import Calculator
import pytest

def test_calculator_methods_basic():
    c = Calculator()
    assert c.add(2, 3) == 5
    assert c.sub(5, 2) == 3
    assert c.mul(4, 2.5) == 10.0
    assert c.div(10, 2) == 5

def test_calculator_div_zero_raises():
    c = Calculator()
    with pytest.raises(ZeroDivisionError):
        c.div(1, 0)
