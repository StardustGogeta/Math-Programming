from sympy import binomial as C
from math import floor, sqrt

def squareFree(n):
    if n == 1: return True
    sq = sqrt(n)
    if not sq % 1: return False
    for d in range(2, floor(sqrt(sq))+2):
        if not n % d**2: return False
    return True

S = 0
added = set()
for n in range(51):
    for k in range(n+1):
        val = C(n, k)
        if val not in added:
            if squareFree(val):
                S += val
            added.add(val)
        else:
            pass
print(S)
