import math, time
##def prime(n):
##    for d in range(2, math.floor(math.sqrt(n))+1):
##        if not n % d: return False
##    return True
##
##def primeSieve(N):
##    allNums = range(2, N)
##    primes = []
##    for n in allNums:
##        passing = True
##        for p in primes:
##            if p > math.sqrt(n):
##                break
##            if not n % p:
##                passing = False
##                break
##        if passing:
##            primes.append(n)
##    return primes

# O(n) versus O(n^2) in other primality checks above
def efficientSieve(N):
    allNums = list(range(2, N))
    primes = []
    for i in range(len(allNums)):
        n = allNums[i]
        if n:
            for j in range(i+n, len(allNums), n):
                allNums[j] = 0
    return list(filter(lambda x: x, allNums))

start = time.perf_counter()
N = 10**8
primes = efficientSieve(N//2)
compos = set()
for i in range(len(primes)):
    for j in range(i, len(primes)):
        mul = primes[i]*primes[j]
        if mul < N: compos.add(mul)
        else: break
print(len(compos), time.perf_counter()-start)

##n = 10**6
##start = time.perf_counter()
##p = list(filter(prime, range(2, n)))
##print(time.perf_counter()-start)
##
##start = time.perf_counter()
##p2 = primeSieve(n)
##print(time.perf_counter()-start, p2==p)
##
##start = time.perf_counter()
##p3 = efficientSieve(n)
##print(time.perf_counter()-start, p3==p2)
