import time

def fac(n):
    ret = 1
    for x in range(2, n+1): ret *= x
    return ret

digitFacs = [fac(n) for n in range(10)]

def sumFacDigits(n):
    ret = 0
    while n:
        ret += digitFacs[n % 10]
        #ret += fac(n % 10)
        n //= 10
    return ret

cache = dict()
def chainLen(n):
    if n in cache: return cache[n]
    if n in [169, 363601, 1454]:
        return 3
    if n in [871, 45361, 872, 45362]:
        return 2
    x = sumFacDigits(n)
    if n == x: return 1
    ret = 1 + chainLen(x)
    cache[n] = ret
    return ret

s = time.perf_counter()
for x in range(3, 10**6):
    try:
        chainLen(x)
    except: print(x)
print(list(cache.values()).count(60))
print(time.perf_counter()-s)
