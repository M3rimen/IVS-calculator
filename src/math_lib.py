
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b  

def div(a,b):
    if b==0:
        return 0 #error 
    return a/b

def fact(n):
    if n<0:
        return 0 #error
    if n==0:
        return 1
    return n*fact(n-1)

def compute_e(precision=20):
    e = 1  
    for i in range(1, precision):
        e += 1 / fact(i) 
    return e

def arctan(x, precision=1e-17): # Fast arctan for Machin-like pi
    term = x
    result = x
    n = 1
    while abs(term) > precision:
        term *= -x*x
        result += term / (2*n + 1)
        n += 1
    return result

# Machin formula: π = 4*(4*arctan(1/5) − arctan(1/239))
def pi(precision=1e-17):
    return 4 * (4*arctan(1/5, precision) - arctan(1/239, precision))

def square(a):
    return a*a

def cube(a):
    return a*a*a

def power(a,b):
    return a**b

def sqrt(a):
    if a < 0:
        return -1
    # compute float root
    res = a**0.5
    # round to 10 decimal places for display
    res = round(res, 10)
    # if it's essentially an exact square, snap to integer
    rint = round(res)
    if abs(rint*rint - a) < 1e-10:
        return rint
    return res

def cbrt(a):
    if a < 0:
        res = -((-a)**(1/3))
    else:
        res = a**(1/3)
    # round to 10 decimal places
    res = round(res, 10)
    # snap perfect cubes to integer
    rint = round(res)
    if abs(rint**3 - a) < 1e-10:
        return rint
    return res

def nthroot(a,n):
    if a < 0:
        res = -((-a)**(1/3))
    else:
        res = a**(1/3)
    # snap perfect cubes
    rint = round(res)
    if abs(rint**3 - a) < 1e-10:
        return rint
    return res

def ln(a, precision=1e-20):
    if a <= 0:
        return -1  # error
    if a == 1:
        return 0  # ln(1)=0

    #Taylorova expanzia
    if a > 1:
        x = (a - 1) / (a + 1)
        result = 0
        power = x
        i = 1
        while abs(power / i) > precision:  
            result += power / i
            power *= x * x  # (a - 1)/(a + 1) ^ (2n+1)
            i += 2
        return 2 * result  # Výsledok je vynásobený 2
    else:
        return -ln(1/a, precision)

def log(a,b):
    if a <= 0:
        return -1
    if b <= 0 or b == 1:
        return -1
    return ln(a)/ln(b)

def abs(a):
    if a<0:
        return -a
    return a

# Helper: snap tiny errors to exact integer
def _snap_to_integer(val, precision):
    nearest = round(val)
    if abs(val - nearest) < precision:
        return float(nearest)
    return val

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

def tg(x, precision=1e-17):
    c_val = cos(x, precision)
    if abs(c_val) < precision:
        return float('inf')
    return _snap_to_integer(sin(x, precision) / c_val, precision)

def cotg(x, precision=1e-17):
    s_val = sin(x, precision)
    if abs(s_val) < precision:
        return float('inf')
    return _snap_to_integer(cos(x, precision) / s_val, precision)
