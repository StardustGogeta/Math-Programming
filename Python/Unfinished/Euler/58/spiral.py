import math
def newDiags(n):
    n2, delta = n**2, n-1
    return [n2-3*delta, n2-2*delta, n2-delta, n2]
def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True

total = 1
primeCount = 0
for n in range(3, 900001, 2):
    total += 4
    primeCount += sum(map(prime, newDiags(n)))
    if primeCount / total < .1 and primeCount:
        print(n, primeCount / total)
        break

