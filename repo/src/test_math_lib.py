import math  # Importing standard math module for comparison
import math_lib  # Importing the custom math library to be tested

## @brief Test addition functionality from math_lib
## @details Verifies correct results for positive, negative, and floating-point additions
def test_add():
    assert math_lib.add(1, 2) == 3
    assert math_lib.add(-5, 5) == 0
    assert math_lib.add(3.2, 4.8) == 8.0

## @brief Test subtraction functionality
## @details Validates subtraction for various positive and negative values including floats
def test_sub():
    assert math_lib.sub(10, 5) == 5
    assert math_lib.sub(0, 5) == -5
    assert math_lib.sub(3.5, 1.2) == 2.3

## @brief Test multiplication functionality
## @details Includes tests with integers, negative numbers and floating-point values
def test_mul():
    assert math_lib.mul(3, 4) == 12
    assert math_lib.mul(-2, 6) == -12
    assert math_lib.mul(2.5, 4) == 10.0

## @brief Test division functionality
## @details Tests normal division, floating-point division, and division by zero
def test_div():
    assert math_lib.div(10, 2) == 5
    assert math_lib.div(7, 2) == 3.5
    assert math_lib.div(5, 0) == "Error"  # Handle divide by zero gracefully

## @brief Test factorial computation
## @details Checks correct calculation for 0, positive integers and handling of negative inputs
def test_fact():
    assert math_lib.fact(0) == 1
    assert math_lib.fact(5) == 120
    assert math_lib.fact(-3) == "Error"

## @brief Test Euler's number approximation
## @details Compares custom approximation with Python’s math.e constant
def test_compute_e():
    e_approx = math_lib.compute_e(precision=10)
    assert math.isclose(e_approx, math.e, rel_tol=1e-6)

## @brief Test arctangent and pi approximation
## @details Validates arctan result and compares custom pi approximation with math.pi
def test_arctan_and_pi():
    arctan_half = math_lib.arctan(0.5)
    assert math.isclose(arctan_half, math.atan(0.5), rel_tol=1e-10)
    pi_approx = math_lib.pi()
    assert math.isclose(pi_approx, math.pi, rel_tol=1e-10)

## @brief Test squaring and exponentiation
## @details Verifies squaring a number and raising to various powers
def test_square_and_power():
    assert math_lib.square(5) == 25
    assert math_lib.power(2, 3) == 8
    assert math_lib.power(5, 0) == 1

## @brief Test square root functionality
## @details Checks for perfect square, irrational square root and negative number handling
def test_sqrt():
    assert math_lib.sqrt(4) == 2
    assert math_lib.sqrt(2) == round(math.sqrt(2), 10)
    assert math_lib.sqrt(-1) == "Error"

## @brief Test n-th root computation
## @details Tests for positive/negative inputs, even/odd roots, and invalid inputs
def test_nthroot():
    assert math_lib.nthroot(27, 3) == 3
    assert math.isclose(math_lib.nthroot(16, 4), 2.0, rel_tol=1e-10)
    assert math_lib.nthroot(-8, 3) == -2
    assert math_lib.nthroot(-16, 4).startswith("Error")
    assert math_lib.nthroot(8, 0).startswith("Error")

## @brief Test natural logarithm and logarithm with custom base
## @details Includes valid and invalid input handling for ln and log
def test_ln_and_log():
    assert math_lib.ln(1) == 0
    assert math.isclose(math_lib.ln(math.e), 1.0, rel_tol=1e-10)
    assert math_lib.ln(0) == "Error"
    assert math.isclose(math_lib.log(8, 2), 3, rel_tol=1e-10)
    assert math_lib.log(-1, 10) == "Error"
    assert math_lib.log(10, 1) == "Error"

## @brief Test absolute value and list summation
## @details Tests abs for positive/negative numbers and sum over lists, including empty list
def test_abs_sum():
    assert math_lib.abs(-5) == 5
    assert math_lib.abs(3) == 3
    assert math_lib.sum([1, 2, 3, 4]) == 10
    assert math_lib.sum([]) == 0

## @brief Test trigonometric functions: sin, cos, tan, cotangent
## @details Validates results for known angles and handles undefined cases
def test_sin_cos_tg_cotg():
    assert math.isclose(math_lib.sin(30), 0.5, rel_tol=1e-10)
    assert math.isclose(math_lib.cos(60), 0.5, rel_tol=1e-10)
    assert math.isclose(math_lib.tg(45), 1, rel_tol=1e-10)
    assert math.isclose(math_lib.cotg(45), 1, rel_tol=1e-10)
    assert math_lib.tg(90) == "Error"
    assert math_lib.cotg(0) == "Error"

## @brief Final test result output
## @details Printed if all assertions above pass successfully
print("All tests passed!")
