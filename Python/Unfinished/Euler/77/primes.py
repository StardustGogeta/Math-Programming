import math, time
def prime(n):
    if n < 2: return False
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d:
            return False
    return True

def findMaxWays(n, threshold = 0):
    if not threshold:
        if n in maxWays: return maxWays[n]
        threshold = n
    if n < 4 and threshold >= n: return maxWays[n]
    w = 0
    highestP = next(p for p in primes[::-1] if p < n and p <= threshold)
    for i in range(primes.index(highestP), -1, -1):
        p = primes[i]
        w += findMaxWays(n-p, p)
    if threshold >= n:
        if n in primes: w += 1
        maxWays[n] = w
    return w

start = time.perf_counter()
maxWays = dict()
primes = list(filter(prime, range(2, 100)))
maxWays[1] = 0
maxWays[2] = 1
maxWays[3] = 1
print(next(x for x in range(10,100) if findMaxWays(x) > 5000))
print(time.perf_counter()-start)
