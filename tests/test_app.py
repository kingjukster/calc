import math
import pytest
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.append(str(root / "src"))

import app


def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(5, 2) == 3

def test_multiply():
    assert app.multiply(3, 4) == 12

def test_divide_normal():
    assert app.divide(10, 2) == 5

def test_divide_zero():
    with pytest.raises(ValueError):
        app.divide(1, 0)

def test_square():
    assert app.square(5) == 25

def test_square_root():
    assert app.square_root(9) == 3

def test_square_root_negative():
    with pytest.raises(ValueError):
        app.square_root(-1)

def test_log_normal():
    assert app.log_value(math.e) == pytest.approx(1)

def test_log_error():
    # x <= 0
    with pytest.raises(ValueError):
        app.log_value(0)
    # invalid base
    with pytest.raises(ValueError):
        app.log_value(10, 1)

def test_sine_cosine():
    assert app.sine(0) == pytest.approx(0)
    assert app.cosine(0) == pytest.approx(1)

def test_percentage():
    assert app.percentage(200, 10) == 20
