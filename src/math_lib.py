#

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

def mod(a,b):
    return a%b

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

def pi(precision=10000000):
    pi = 0.0
    for i in range(precision):
        pi += ((-1)**i) / (2*i + 1)
    return 4 * pi

def power(a,b):
    return a**b

def sqrt(a):
    if a<0:
        return -1 #error
    return a**0.5

def cbrt(a):
    if a<0:
        return -1
    return a**(1/3)

def nthroot(a,n):
    if a<0:
        return -1
    return a**(1/n)

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

def convert_number(a, flag):
    if flag == 1:  # Binary to Decimal (2 -> 10)
        b = 0
        c = 0
        while a != 0:
            d = a % 10
            b += d * (2 ** c)
            a = a // 10
            c += 1
        return b

    elif flag == 2:  # Decimal to Binary (10 -> 2)
        if a == 0:
            return 0
        digits = []
        while a != 0:
            digits.append(str(a % 2))
            a //= 2
        return int(''.join(digits[::-1]))  # Reverse and join as a string, then convert to integer

    elif flag == 3:  # Decimal to Octal (10 -> 8)
        if a == 0:
            return 0
        digits = []
        while a != 0:
            digits.append(str(a % 8))
            a //= 8
        return int(''.join(digits[::-1]))

    elif flag == 4:  # Octal to Decimal (8 -> 10)
        b = 0
        c = 0
        while a != 0:
            d = a % 10
            b += d * (8 ** c)
            a //= 10
            c += 1
        return b

    else:
        return "Invalid flag"

def sin(x, precision=1e-10):
    result = 0
    term = x
    n = 1
    while abs(term) > precision:
        result += term
        term *= -x**2 / (fact(2*n) * fact(2*n + 1))  # Use the fact function here
        n += 1
    return result

def cos(x, precision=1e-10):
    result = 1
    term = 1
    n = 1
    while abs(term) > precision:
        term *= -x**2 / (fact(2*n - 1) * fact(2*n))  # Use the fact function here
        result += term
        n += 1
    return result

def tg(x, precision=1e-10):
    cos_x = cos(x, precision)
    if cos_x == 0:
        return float('inf')  # Undefined when cos(x) = 0
    return sin(x, precision) / cos_x

def cotg(x, precision=1e-10):
    sin_x = sin(x, precision)
    if sin_x == 0:
        return float('inf')  # Undefined when sin(x) = 0
    return cos(x, precision) / sin_x
