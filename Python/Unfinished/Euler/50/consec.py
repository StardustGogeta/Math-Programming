import math

def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True

primes = list(filter(prime, range(2, 10**5)))
M = (0,0)
for y in range(100):
    total = 0
    n = 0
    for x in primes[y:]:
        if prime(total) and n > M[1]:
            M = (total, n)
        total += x
        n += 1
        if total > 10**6: break
print(M)
