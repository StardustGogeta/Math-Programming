import math

def sumOfDigits(n):
    return sum(int(x) for x in str(n))
def f(n):
    return sum(math.factorial(int(x)) for x in str(n))
def sf(n):
    return sumOfDigits(f(n))
def g(i):
    n = 1
    while sf(n) != i: n += 1
    return n
def sg(i):
    return sumOfDigits(g(i))

assert f(342) == 32
assert sf(342) == 5
assert sf(25) == 5
assert g(5) == 25
assert sg(5) == 7
assert g(20) == 267
assert sum(sg(i) for i in range(1, 21)) == 156

fL = lambda n: math.floor(math.log10(n))
def f_approx(n): # Maybe is good? Who knows?
    return 40000*(fL(n)+1)
def sf_approx(n): # Maybe is good? Who knows?
    return 5*fL(40000*(fL(n)+1))
def sfUpperBound(n): # Tested to work for at least 1 through 10**6, should be guaranteed to work
    return 9*(fL(362880*(fL(n)+1))+1)
def sfLowerBound(n): # Tested to work for at least 1 through 10**6, should almost always work
    return fL(fL(n)+1)+1
def sgLowerBound(i): # Tested to work for at least 1 through 40, should almost always work
    return 10**((i-9)/9)/362880
def sgUpperBound(i): # Tested to work for at least 1 through 40, should almost always work
    return 10**i
def sgUpperBound2(i): # Tested to work for at least 1 through 40 (except for 3), should almost always work
    return 10**(i/5)



