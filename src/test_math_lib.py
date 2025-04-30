import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import math
from math_lib import *

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
    assert div(5, 0) == 0  # Pôvodná funkcia vracia 0 pri delení nulou
    assert div(7, 2) == 3.5

    # fact
    assert fact(0) == 1
    assert fact(5) == 120
    assert fact(-3) == 0  # Pôvodná funkcia vracia 0 pre záporné čísla

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
    assert sqrt(-4) == -1  # Pôvodná funkcia vracia -1 pre záporné čísla

    # nthroot
    assert round(nthroot(16, 4), 5) == 2
    assert round(nthroot(81, 4), 5) == 3
    assert nthroot(-4, 2) == -1  # Pôvodná funkcia vracia -1 pre záporné čísla

    # ln
    assert abs(ln(math.e) - 1) < 0.01
    assert ln(0) == -1  # Pôvodná funkcia vracia -1 pre nulu
    assert ln(-1) == -1  # Pôvodná funkcia vracia -1 pre záporné čísla

    # log
    assert abs(log(100, 10) - 2) < 0.01
    assert log(0, 10) == -1  # Pôvodná funkcia vracia -1 pre nulu
    assert log(10, 1) == -1  # Pôvodná funkcia vracia -1 pre základ 1
    assert log(10, 2) == 3.321928094887362

    # abs
    assert abs(-4) == 4
    assert abs(5) == 5

    # sin
    assert abs(sin(90) - 1) < 0.01  # Pôvodná funkcia očakáva stupne

    # cos
    assert abs(cos(180) + 1) < 0.01  # Pôvodná funkcia očakáva stupne

    # tg
    assert abs(tg(45) - 1) < 0.01  # Pôvodná funkcia očakáva stupne

    # cotg
    assert abs(cotg(45) - 1) < 0.01  # Pôvodná funkcia očakáva stupne
