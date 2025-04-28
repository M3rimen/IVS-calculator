import pytest
import math
from src.math_lib import *

def test_calculator():
    # add
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    assert add(0, 0) == 0

    # sub
    assert sub(5, 2) == 3
    assert sub(0, 5) == -5
    assert sub(-3, -3) == 0

    # mul
    assert mul(3, 4) == 12
    assert mul(-2, 3) == -6
    assert mul(0, 100) == 0

    # div
    assert div(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
    assert div(7, 2) == 3.5

    # fact
    assert fact(0) == 1
    assert fact(5) == 120
    assert fact(-3) == 0

    # compute_e
    assert abs(compute_e(10) - math.e) < 0.01
    assert abs(compute_e(20) - math.e) < 0.001
    assert abs(compute_e(5) - 2.7166666666666663) < 0.01

    # pi
    assert abs(pi(1000) - math.pi) < 0.01
    assert abs(pi(10000) - math.pi) < 0.001
    assert abs(pi(100000) - math.pi) < 0.0001

    # power
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -2) == 0.25

    # sqrt
    assert sqrt(9) == 3
    assert sqrt(0) == 0
    with pytest.raises(ValueError):
        sqrt(-4)

    # cbrt
    assert round(cbrt(27), 5) == 3
    assert round(cbrt(0), 5) == 0
    assert cbrt(-8) == -1

    # nthroot
    assert round(nthroot(16, 4), 5) == 2
    assert round(nthroot(81, 4), 5) == 3
    with pytest.raises(ValueError):
        nthroot(-4, 2)

    # ln
    assert abs(ln(math.e) - 1) < 0.01

    # log
    assert abs(log(100, 10) - 2) < 0.01
    with pytest.raises(ValueError):
        log(0, 10)
    assert log(10, 2) == 3.321928094887362

    # abs
    assert abs(-4) == 4
    assert abs(5) == 5
    
    # convert_number
    #assert convert_number(12, 4) == 14
    #assert convert_number(1010, 2) == 10
    #assert convert_number(10, 3) == 11

    # sin
    assert abs(sin(math.pi/2) - 1) < 0.01

    # cos
    assert abs(cos(math.pi) + 1) < 0.01

    # tg
    assert abs(tg(math.pi/4) - 1) < 0.01

    # cotg
    assert abs(cotg(math.pi/4) - 1) < 0.01
