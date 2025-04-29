def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b  

def div(a,b):
    if b==0:
        return "Error"
    return a/b

def fact(n):
    if n<0:
        return "Error"
    if n==0:
        return 1
    return n*fact(n-1)

def compute_e(precision=20):
    e = 1  
    for i in range(1, precision):
        e += 1 / fact(i) 
    return e

def arctan(x, precision=1e-17):
    term = x
    result = x
    n = 1
    while abs(term) > precision:
        term *= -x*x
        result += term / (2*n + 1)
        n += 1
    return result

def pi(precision=1e-17):
    return 4 * (4*arctan(1/5, precision) - arctan(1/239, precision))

def square(a):
    return a*a

def power(a,b):
    return a**b

def sqrt(a):
    if a < 0:
        return "Error"
    res = a**0.5
    res = round(res, 10)
    rint = round(res)
    if abs(rint*rint - a) < 1e-10:
        return rint
    return res

def nthroot(a,n):
    if n%2 == 0 and a < 0:
        return "Error"
    if a < 0:
        res = -((-a)**(1/3))
    else:
        res = a**(1/3)
    rint = round(res)
    if abs(rint**3 - a) < 1e-10:
        return rint
    return res

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

def log(a,b):
    if a <= 0 or b <= 0 or b == 1:
        return "Error"
    return ln(a)/ln(b)

def abs(a):
    return -a if a<0 else a

def _snap_to_integer(val, precision):
    nearest = round(val)
    return float(nearest) if abs(val - nearest) < precision else val

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

def tg(x, precision=1e-10):
    cos_x = cos(x, precision)
    if cos_x == 0:
        return float('inf')
    return sin(x, precision) / cos_x

def cotg(x, precision=1e-10):
    sin_x = sin(x, precision)
    if sin_x == 0:
        return float('inf')
    return cos(x, precision) / sin_x

def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
