import math
from math_lib import *

def test_calculator():
    # add
    try:
        assert add(2, 3) == 5
        print("Test: passed! = add(2, 3)")
    except AssertionError:
        print("Test: failed! = add(2, 3)")

    try:
        assert add(-1, 5) == 4
        print("Test: passed! = add(-1, 5)")
    except AssertionError:
        print("Test: failed! = add(-1, 5)")

    try:
        assert add(0, 0) == 0
        print("Test: passed! = add(0, 0)")
    except AssertionError:
        print("Test: failed! = add(0, 0)")

    # sub
    try:
        assert sub(5, 2) == 3
        print("Test: passed! = sub(5, 2)")
    except AssertionError:
        print("Test: failed! = sub(5, 2)")

    try:
        assert sub(0, 5) == -5
        print("Test: passed! = sub(0, 5)")
    except AssertionError:
        print("Test: failed! = sub(0, 5)")

    try:
        assert sub(-3, -3) == 0
        print("Test: passed! = sub(-3, -3)")
    except AssertionError:
        print("Test: failed! = sub(-3, -3)")

    # mul
    try:
        assert mul(3, 4) == 12
        print("Test: passed! = mul(3, 4)")
    except AssertionError:
        print("Test: failed! = mul(3, 4)")

    try:
        assert mul(-2, 3) == -6
        print("Test: passed! = mul(-2, 3)")
    except AssertionError:
        print("Test: failed! = mul(-2, 3)")
        
    try:
        assert mul(0, 100) == 0
        print("Test: passed! = mul(0, 100)")
    except AssertionError:
        print("Test: failed! = mul(0, 100)")

    # div
    try:
        assert div(10, 2) == 5
        print("Test: passed! = div(10, 2)")
    except AssertionError:
        print("Test: failed! = div(10, 2)")

    try:
        assert div(5, 0) == 0
        print("Test: passed! = div(5, 0)")
    except AssertionError:
        print("Test: failed! = div(5, 0)")

    try:
        assert div(7, 2) == 3.5
        print("Test: passed! = div(7, 2)")
    except AssertionError:
        print("Test: failed! = div(7, 2)")

    # mod
    try:
        assert mod(10, 3) == 1
        print("Test: passed! = mod(10, 3)")
    except AssertionError:
        print("Test: failed! = mod(10, 3)")

    try:
        assert mod(7, 7) == 0
        print("Test: passed! = mod(7, 7)")
    except AssertionError:
        print("Test: failed! = mod(7, 7)")

    try:
        assert mod(5, 2) == 1
        print("Test: passed! = mod(5, 2)")
    except AssertionError:
        print("Test: failed! = mod(5, 2)")

    # fact
    try:
        assert fact(0) == 1
        print("Test: passed! = fact(0)")
    except AssertionError:
        print("Test: failed! = fact(0)")

    try:
        assert fact(5) == 120
        print("Test: passed! = fact(5)")
    except AssertionError:
        print("Test: failed! = fact(5)")

    try:
        assert fact(-3) == 0
        print("Test: passed! = fact(-3)")
    except AssertionError:
        print("Test: failed! = fact(-3)")

    # compute_e
    try:
        assert abs(compute_e(10) - math.e) < 0.01
        print("Test: passed! = compute_e(10)")
    except AssertionError:
        print("Test: failed! = compute_e(10)")

    try:
        assert abs(compute_e(20) - math.e) < 0.001
        print("Test: passed! = compute_e(20)")
    except AssertionError:
        print("Test: failed! = compute_e(20)")

    try:
        assert abs(compute_e(5) - 2.7166666666666663) < 0.01
        print("Test: passed! = compute_e(5)")
    except AssertionError:
        print("Test: failed! = compute_e(5)")

    # pi
    try:
        assert abs(pi(1000) - math.pi) < 0.01
        print("Test: passed! = pi(1000)")
    except AssertionError:
        print("Test: failed! = pi(1000)")

    try:
        assert abs(pi(10000) - math.pi) < 0.001
        print("Test: passed! = pi(10000)")
    except AssertionError:
        print("Test: failed! = pi(10000)")

    try:
        assert abs(pi(100000) - math.pi) < 0.0001
        print("Test: passed! = pi(100000)")
    except AssertionError:
        print("Test: failed! = pi(100000)")

    # power
    try:
        assert power(2, 3) == 8
        print("Test: passed! = power(2, 3)")
    except AssertionError:
        print("Test: failed! = power(2, 3)")

    try:
        assert power(5, 0) == 1
        print("Test: passed! = power(5, 0)")
    except AssertionError:
        print("Test: failed! = power(5, 0)")

    try:
        assert power(2, -2) == 0.25
        print("Test: passed! = power(2, -2)")
    except AssertionError:
        print("Test: failed! = power(2, -2)")

    # sqrt
    try:
        assert sqrt(9) == 3
        print("Test: passed! = sqrt(9)")
    except AssertionError:
        print("Test: failed! = sqrt(9)")

    try:
        assert sqrt(0) == 0
        print("Test: passed! = sqrt(0)")
    except AssertionError:
        print("Test: failed! = sqrt(0)")

    try:
        assert sqrt(-4) == -1
        print("Test: passed! = sqrt(-4)")
    except AssertionError:
        print("Test: failed! = sqrt(-4)")

    # cbrt
    try:
        assert round(cbrt(27), 5) == 3
        print("Test: passed! = cbrt(27)")
    except AssertionError:
        print("Test: failed! = cbrt(27)")

    try:
        assert round(cbrt(0), 5) == 0
        print("Test: passed! = cbrt(0)")
    except AssertionError:
        print("Test: failed! = cbrt(0)")

    try:
        assert cbrt(-8) == -1
        print("Test: passed! = cbrt(-8)")
    except AssertionError:
        print("Test: failed! = cbrt(-8)")

    # nthroot
    try:
        assert round(nthroot(16, 4), 5) == 2
        print("Test: passed! = nthroot(16, 4)")
    except AssertionError:
        print("Test: failed! = nthroot(16, 4)")

    try:
        assert round(nthroot(81, 4), 5) == 3
        print("Test: passed! = nthroot(81, 4)")
    except AssertionError:
        print("Test: failed! = nthroot(81, 4)")

    try:
        assert nthroot(-4, 2) == -1
        print("Test: passed! = nthroot(-4, 2)")
    except AssertionError:
        print("Test: failed! = nthroot(-4, 2)")

    # ln
    try:
        assert abs(ln(math.e) - 1) < 0.01
        print("Test: passed! = ln(math.e)")
    except AssertionError:
        print("Test: failed! = ln(math.e)")

    # log
    try:
        assert abs(log(100, 10) - 2) < 0.01
        print("Test: passed! = log(100, 10)")
    except AssertionError:
        print("Test: failed! = log(100, 10)")

    try:
        assert log(0, 10) == -1
        print("Test: passed! = log(0, 10)")
    except AssertionError:
        print("Test: failed! = log(0, 10)")

    try:
        assert log(10, 2) == 3.321928094887362
        print("Test: passed! = log(10, 2)")
    except AssertionError:
        print("Test: failed! = log(10, 2)")

    # abs
    try:
        assert abs(-4) == 4
        print("Test: passed! = abs(-4)")
    except AssertionError:
        print("Test: failed! = abs(-4)")

    try:
        assert abs(5) == 5
        print("Test: passed! = abs(5)")
    except AssertionError:
        print("Test: failed! = abs(5)")

    # convert_number
    try:
        assert convert_number(12, 4) == 14
        print("Test: passed! = convert_number(12, 4)")
    except AssertionError:
        print("Test: failed! = convert_number(12, 4)")

    try:
        assert convert_number(1010, 2) == 10
        print("Test: passed! = convert_number(1010, 2)")
    except AssertionError:
        print("Test: failed! = convert_number(1010, 2)")

    try:
        assert convert_number(10, 3) == 11
        print("Test: passed! = convert_number(10, 3)")
    except AssertionError:
        print("Test: failed! = convert_number(10, 3)")

    # sin
    try:
        assert abs(sin(math.pi/2) - 1) < 0.01
        print("Test: passed! = sin(math.pi/2)")
    except AssertionError:
        print("Test: failed! = sin(math.pi/2)")

    # cos
    try:
        assert abs(cos(math.pi) + 1) < 0.01
        print("Test: passed! = cos(math.pi)")
    except AssertionError:
        print("Test: failed! = cos(math.pi)")

    # tg
    try:
        assert abs(tg(math.pi/4) - 1) < 0.01
        print("Test: passed! = tg(math.pi/4)")
    except AssertionError:
        print("Test: failed! = tg(math.pi/4)")

    # cotg
    try:
        assert abs(cotg(math.pi/4) - 1) < 0.01
        print("Test: passed! = cotg(math.pi/4)")
    except AssertionError:
        print("Test: failed! = cotg(math.pi/4)")

test_calculator()
