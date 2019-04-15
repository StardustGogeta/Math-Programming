import math
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
##            #print(n)
##    return primes

def efficientSieve(N):
    allNums = list(range(2, N))
    primes = []
    for i in range(len(allNums)):
        n = allNums[i]
        if n:
            for j in range(i+n, len(allNums), n):
                allNums[j] = 0
    return list(filter(lambda x: x, allNums))

def divisibleByOnly(p,q,n):
##    r = p * q
##    if n % r: return False
##    #while not n % r: n //= r
    while not n % p: n //= p
    while not n % q: n //= q
    return n == 1

def M(p, q, N):
    if p * q > N: return 0
    greatestUnder = p * q * (N // (p*q))
    for n in range(greatestUnder, p*q-1, -p*q):
        if divisibleByOnly(p, q, n): return n
    print(p, q, N, greatestUnder)

def S(N):
    s = 0
    #primes = list(filter(prime, range(2, N//2)))
    primes = efficientSieve(N//2)
    print("primes ready")
    for x0 in range(len(primes)-1):
        for x1 in range(x0+1, len(primes)):
            s += M(primes[x0], primes[x1], N)
    return s
