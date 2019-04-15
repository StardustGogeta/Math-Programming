from math import sqrt, ceil, floor
def prime(n):
    if n < 2: return False
    for d in range(2, floor(sqrt(n))+1):
        if not n % d: return False
    return True

def findY(x, D):
    y = sqrt((x**2-1)/D)
    if y % 1: return -1
    else: return y

def findX(D, lim=True):
    x = ceil(sqrt(D))
    if x**2 == D: return -1
    inc = 1
    if D & 1 == 0:
        if x & 1 == 0: x += 1
        inc += 1
    while findY(x, D) < 0:
        if lim and x == 1000000: break
        x += inc
    return x

def findX2Help(y, D):
    x = ceil(sqrt(1+D*y**2))
    if x**2-D*y**2 != 1: return -1
    return x

def findX2(D):
    y = 1
    if not sqrt(D) % 1: return -1
    while findX2Help(y, D) < 0:
        y += 1
    return findX2Help(y, D)

M = 100
primes = [D for D in range(M + 1) if prime(D)]
xs = [findX2(D) for D in range(M + 1) if prime(D)]
print(primes, xs)
print(primes[xs.index(max(xs))])
