import math, time
def efficientSieve(N):
    allNums = list(range(2, N))
    primes = []
    for i in range(len(allNums)):
        n = allNums[i]
        if n:
            for j in range(i+n, len(allNums), n):
                allNums[j] = 0
    return list(filter(lambda x: x, allNums))

def S(p):
    if p < 100: return S2(p)
    firstFact = math.factorial(p-5) % p
    s = firstFact
    n = 1
    #for m in (2, 6, 24, 120):
    for m in range(p-4, p+1):
        n *= m
        s += firstFact * n
    return (s % p)

def S2(p):
    return sum(math.factorial(p-k)%p for k in range(1, 6)) % p

def S3(p):
    if p < 100: return S2(p)
    firstFact = math.factorial(p-5) % p
##    s = firstFact
##    for m in (2, 6, 24, 120):
##        s += firstFact * m
##    return (s % p) + 6
    return (153*firstFact+6) % p

#print(S(7))
#start = time.perf_counter()
#print(sum(S(p) for p in efficientSieve(10**4)[2:]))
#print(time.perf_counter()-start)
for p in efficientSieve(10**4)[2:]:
    #print("test")
    #print(p)
    start = time.perf_counter()
    s = S(p)
    end = time.perf_counter() - start
    start2 = time.perf_counter()
    s2 = S2(p)
    end2 = time.perf_counter() - start2
    start3 = time.perf_counter()
    s3 = S3(p)
    end3 = time.perf_counter() - start3
    #if s2 != s3: print(p)
    if 6800 > p > 6500: print(p, s, s2, s3, end, end2, end3)
