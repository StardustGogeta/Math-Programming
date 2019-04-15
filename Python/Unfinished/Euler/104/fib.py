from decimal import *
getcontext().prec = 20

phi = (1 + Decimal(5).sqrt())/2

def naive_fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)

def fib(n):
    n -= 1
    f = 1
    g = 1
    for x in range(n//4):
        #F = f + g
        #G = F + g
        f, g = f+g, f+2*g
    if n % 2: return g
    return f

def quick_fib(n):
    return round(phi**n/Decimal(5).sqrt())

def trun_fib(n):
    n -= 1
    f = 1
    g = 1
    for x in range(n//4):
        #F = f + g
        #G = F + g
        f, g = (f+g)%10**9, (f+2*g)%10**9
    if n % 2: return g
    return f

for x in range(10**5):
    s = str(quick_fib(x))
    if sorted(s[:9]) == list('123456789'):
        print(x)
        s2 = str(trun_fib(x))
        print(sorted(s2))
        if sorted(s2) == list('123456789'):
            print(x)
            break
