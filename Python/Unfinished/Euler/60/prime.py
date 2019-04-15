import math, time
verifiedPrime = set()
def prime(n):
    if n == 5: return False
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True

start = time.perf_counter()
primes = list(filter(prime, range(3,10**4,2)))
def validPair(p1, p2):
    s1 = str(p1)
    s2 = str(p2)
    return prime(int(s1+s2)) and prime(int(s2+s1))

minSum = 10**10
L = len(primes)
for x0 in range(L-4):
    p0 = primes[x0]
    for x1 in range(x0, L-3):
        p1 = primes[x1]
        if not validPair(p0, p1): continue
        select = [p0, p1]
        for x2 in range(x1, L-2):
            p2 = primes[x2]
            if not all(validPair(p, p2) for p in select): continue
            select += [p2]
            for x3 in range(x2, L-1):
                p3 = primes[x3]
                if not all(validPair(p, p3) for p in select): continue
                select += [p3]
                for x4 in range(x3, L):
                    p4 = primes[x4]
                    if not all(validPair(p, p4) for p in select): continue
                    select += [p4]
                    minSum = min(minSum, sum(select))
                    print(select, sum(select))
print("MIN:",minSum, time.perf_counter()-start)



