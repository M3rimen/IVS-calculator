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

def ln(a, precision=1e-12):
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