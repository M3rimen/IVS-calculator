import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from calculator import evaluate

def test_evaluate():
    # Simple arithmetic
    assert evaluate('2+3') == 5
    assert evaluate('5-2') == 3
    assert evaluate('3*4') == 12
    assert evaluate('10/2') == 5
    assert evaluate('7/2') == 3.5

    # Power, sqrt, cbrt
    assert evaluate('2**3') == 8
    assert evaluate('sqrt(9)') == 3
    assert evaluate('cbrt(27)') == 3
    assert evaluate('cbrt(-8)') == -2

    # Fact, ln, log
    assert evaluate('fact(5)') == 120
    assert abs(evaluate('ln(2.718281828459045)') - 1) < 0.01
    assert abs(evaluate('log(100,10)') - 2) < 0.01
    assert evaluate('log(0,10)') == -1  # per your math_lib behavior

    # Trigonometry
    assert abs(evaluate('sin(90)') - 1) < 0.01
    assert abs(evaluate('cos(180)') + 1) < 0.01
    assert abs(evaluate('tg(45)') - 1) < 0.01
    assert abs(evaluate('cotg(45)') - 1) < 0.01

    # nthroot and argument commas
    assert evaluate('nthroot(27,3)') == 3
    assert evaluate('nthroot(81,3)') == pytest.approx(4.3267487, rel=1e-5)

    # Pi and e
    assert abs(evaluate('pi()') - 3.141592653589793) < 0.01
    assert abs(evaluate('compute_e(10)') - 2.718281828459045) < 0.01

    # Decimal commas handling
    assert evaluate('3,5+2,5') == 6.0
    assert evaluate('10/2,5') == 4.0

    # Base 2 number system
    assert evaluate('101 + 11', base=2) == 5 + 3

    # Base 8 number system
    assert evaluate('7 + 10', base=8) == 7 + 8

    # Invalid expressions return 0
    assert evaluate('5/0') == 0
    assert evaluate('invalid expression') == 0
