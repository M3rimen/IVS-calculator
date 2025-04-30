import math
import math_lib

def test_add():
    assert math_lib.add(1, 2) == 3
    assert math_lib.add(-5, 5) == 0
    assert math_lib.add(3.2, 4.8) == 8.0


def test_sub():
    assert math_lib.sub(10, 5) == 5
    assert math_lib.sub(0, 5) == -5
    assert math_lib.sub(3.5, 1.2) == 2.3


def test_mul():
    assert math_lib.mul(3, 4) == 12
    assert math_lib.mul(-2, 6) == -12
    assert math_lib.mul(2.5, 4) == 10.0


def test_div():
    assert math_lib.div(10, 2) == 5
    assert math_lib.div(7, 2) == 3.5
    assert math_lib.div(5, 0) == "Error"

def test_fact():
    assert math_lib.fact(0) == 1
    assert math_lib.fact(5) == 120
    assert math_lib.fact(-3) == "Error"

def test_compute_e():
    e_approx = math_lib.compute_e(precision=10)
    assert math.isclose(e_approx, math.e, rel_tol=1e-8)

def test_arctan_and_pi():
    arctan_half = math_lib.arctan(0.5)
    assert math.isclose(arctan_half, math.atan(0.5), rel_tol=1e-10)
    pi_approx = math_lib.pi()
    assert math.isclose(pi_approx, math.pi, rel_tol=1e-10)

def test_square_and_power():
    assert math_lib.square(5) == 25
    assert math_lib.power(2, 3) == 8
    assert math_lib.power(5, 0) == 1

def test_sqrt():
    assert math_lib.sqrt(4) == 2
    assert math_lib.sqrt(2) == round(math.sqrt(2), 10)
    assert math_lib.sqrt(-1) == "Error"

def test_nthroot():
    assert math_lib.nthroot(27, 3) == 3
    assert math.isclose(math_lib.nthroot(16, 4), 2.0, rel_tol=1e-10)
    assert math_lib.nthroot(-8, 3) == -2
    assert math_lib.nthroot(-16, 4).startswith("Error")
    assert math_lib.nthroot(8, 0).startswith("Error")

def test_ln_and_log():
    assert math_lib.ln(1) == 0
    assert math.isclose(math_lib.ln(math.e), 1.0, rel_tol=1e-10)
    assert math_lib.ln(0) == "Error"
    assert math_lib.log(8, 2) == 3
    assert math_lib.log(-1, 10) == "Error"
    assert math_lib.log(10, 1) == "Error"

def test_abs_sum():
    assert math_lib.abs(-5) == 5
    assert math_lib.abs(3) == 3
    assert math_lib.sum([1, 2, 3, 4]) == 10
    assert math_lib.sum([]) == 0

def test_sin_cos_tg_cotg():
    assert math.isclose(math_lib.sin(30), 0.5, rel_tol=1e-10)
    assert math.isclose(math_lib.cos(60), 0.5, rel_tol=1e-10)
    assert math_lib.tg(45) == 1
    assert math_lib.cotg(45) == 1
    assert math_lib.tg(90) == "Error"
    assert math_lib.cotg(0) == "Error"

print("All tests passed!")
