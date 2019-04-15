import math
def findFactor(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return d
    return n
def factorize(n):
    facts = dict()
    while n > 1:
        f = findFactor(n)
        if f in facts:
            facts[f] += 1
        else:
            facts[f] = 1
        n //= f
    return facts
def totient(n):
    facts = factorize(n)
    p = 1
    for f in facts:
        p *= (f-1)*f**(facts[f]-1)
    return p
def efficientSieve(N):
    allNums = list(range(2, N))
    primes = []
    for i in range(len(allNums)):
        n = allNums[i]
        if n:
            for j in range(i+n, len(allNums), n):
                allNums[j] = 0
    return set(filter(lambda x: x, allNums))

cache = {1:1}
def chainLength(n):
    if n in cache: return cache[n]
    L = 1 + chainLength(totient(n))
    cache[n] = L
    return L

def chainLengthMeetsThreshold(n):
    currentLen = 1
    if n in cache: return cache[n] == threshold
    orig = n
    while n != 1:
        n = totient(n)
        if n in cache:
            cache[orig] = currentLen + cache[n]
            return currentLen + cache[n] == threshold
        currentLen += 1
        if n < 281929 and currentLen < 5:
            return False
    cache[orig] = currentLen
    return currentLen == threshold

#print(min(x for x in range(2, 1000000) if chainLength(x) > 19))
threshold = 25
primes = efficientSieve(4*10**7)
print("primed")
s = 0
for p in primes:
    if chainLengthMeetsThreshold(p):
        s += p
print(s)
