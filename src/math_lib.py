## @file math_lib.py
# @brief Library for mathematical operations.
# @date 2025-04-29



## @brief Function to add two numbers.
# @param a first number
# @param b second number
# @return sum
def add(a,b):
    return a+b


## @brief Function to subtract second number from first.
# @param a first number
# @param b second number
# @return difference
def sub(a,b):
    return a-b


## @brief Function to multiply two numbers.
# @param a first number
# @param b second number
# @return product
def mul(a,b):
    return a*b  


## @brief Function to divide first number by second.
# @param a first number
# @param b second number
# @return quotient
# @details If b is 0, returns "Error".
def div(a,b):
    if b==0:
        return "Error"
    return a/b


## @brief Function to calculate factorial of a number.
# @param n number
# @return factorial of n
# @details If n is negative, returns "Error".
def fact(n):
    if n<0:
        return "Error"
    if n==0:
        return 1
    return n*fact(n-1)


## @brief Function to compute the value of Euler's number.
# @param precision number of decimal places
# @details Computation using the Taylor series expansion.
# @return value of euler's number
def compute_e(precision=20):
    e = 1  
    for i in range(1, precision):
        e += 1 / fact(i) 
    return e


## @brief Function to calculate arcus tangens of x.
# @param x number
# @param precision number of decimal places
# @return arctan of x
# @details Computation using the Taylor series expansion.
def arctan(x, precision=1e-17):
    term = x
    result = x
    n = 1
    while abs(term) > precision:
        term *= -x*x
        result += term / (2*n + 1)
        n += 1
    return result


## @brief Function to compute the value of pi.
# @param precision number of decimal places
# @return value of pi
# @details Computation using the Machin-like formula.
def pi(precision=1e-17):
    return 4 * (4*arctan(1/5, precision) - arctan(1/239, precision))

## @brief Function to calculate the square of a number.
# @param a number
# @return square of a
def square(a):
    return a*a

## @brief Function to calculate the power of a number.
# @param a base
# @param b exponent
# @return a raised to the power of b
def power(a,b):
    return a**b


## @brief Function to compute the square root of a number.
# @param a number
# @return square root of a
# @details If a is negative, returns "Error".
def sqrt(a):
    if a < 0:
        return "Error"
    res = a**0.5
    res = round(res, 10)
    rint = round(res)
    if abs(rint*rint - a) < 1e-10:
        return rint
    return res

## @brief Function to compute the nth root of a number.
# @param a number
# @param n root
# @return nth root of a
# @details If a is negative and n is even, returns "Error".
def nthroot(a,n):
    if n%2 == 0 and a < 0:
        return "Error"
    if a < 0:
        res = -((-a)**(1/n))
    else:
        res = a**(1/n)
    rint = round(res)
    if abs(rint**n - a) < 1e-10:
        return rint
    return res


## @brief Function to calculate the natural logarithm of a number.
# @param a number
# @param precision number of decimal places
# @return natural logarithm of a
# @details Computation using the Taylor series expansion.
# @details If a is less than or equal to 0, returns "Error".
def ln(a, precision=1e-20):
    if a <= 0:
        return "Error"
    if a == 1:
        return 0
    if a > 1:
        x = (a - 1) / (a + 1)
        result = 0
        power = x
        i = 1
        while abs(power / i) > precision:  
            result += power / i
            power *= x * x
            i += 2
        return 2 * result
    else:
        return -ln(1/a, precision)


## @brief Function to calculate the logarithm of a number with base b.
# @param a number
# @param b base
# @return logarithm of a with base b
def log(a,b):
    if a <= 0 or b <= 0 or b == 1:
        return "Error"
    return ln(a)/ln(b)


## @brief Function to calculate the absolute value of a number.
# @param a number
# @return absolute value of a
def abs(a):
    return -a if a < 0 else a

## @brief Function to round result into more readable format.
# @param val number
# @param precision number of decimal places
# @return rounded value
# @details Used in some goniometric functions
def _snap_to_integer(val, precision):
    nearest = round(val)
    return float(nearest) if abs(val - nearest) < precision else val


## @brief Function to calculate the sine of an angle in degrees.
# @param x angle in degrees
# @param precision number of decimal places
# @return sine of x
# @details Computation using the Taylor series expansion.
def sin(x, precision=1e-17):
    x = x % 360
    rad = x * pi(precision) / 180
    result = 0.0
    term = rad
    n = 1
    while abs(term) > precision:
        result += term
        term *= -rad*rad / ((2*n) * (2*n + 1))
        n += 1
    return _snap_to_integer(result, precision)


## @brief Function to calculate the cosine of an angle in degrees.
# @param x angle in degrees
# @param precision number of decimal places
# @return cosine of x
# @details Computation using the Taylor series expansion.
def cos(x, precision=1e-17):
    x = x % 360
    rad = x * pi(precision) / 180
    result = 1.0
    term = 1.0
    n = 1
    while abs(term) > precision:
        term *= -rad*rad / ((2*n - 1) * (2*n))
        result += term
        n += 1
    return _snap_to_integer(result, precision)


## @brief Function to calculate the tangent of an angle in degrees.
# @param x angle in degrees
# @param precision number of decimal places
# @return tangent of x
# @details Computation using the sine and cosine functions.
def tg(x, precision=1e-10):
    cos_x = cos(x, precision)
    if cos_x == 0:
        return "Error"
    return sin(x, precision) / cos_x


## @brief Function to calculate the cotangent of an angle in degrees.
# @param x angle in degrees
# @param precision number of decimal places
# @return cotangent of x
# @details Computation using the sine and cosine functions.
def cotg(x, precision=1e-10):
    sin_x = sin(x, precision)
    if sin_x == 0:
        return "Error"
    return cos(x, precision) / sin_x


## @brief Function to calculate the sum of a list of numbers.
# @param numbers list of numbers
# @return sum of numbers
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# end of math_lib.py