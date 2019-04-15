import math
def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d:
            return False
    return True

def primeGenerating(n):
    for d in range(1, math.floor(math.sqrt(n))+1):
        if not n % d:
            if not prime(d+n//d): return False
    return True

print(sum(x for x in range(1, 10**8) if primeGenerating(x)))
