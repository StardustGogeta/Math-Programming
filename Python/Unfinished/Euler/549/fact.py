import math, time
# Approximately O(n), needs improvement
def findFactor(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return d
    return n
prefact = dict()
def factorize(n):
    origN = n
    if n in prefact:
        #print('yay')
        return prefact[n]
    facts = dict()
    while n > 1:
        f = findFactor(n)
        if f in facts:
            facts[f] += 1
        else:
            facts[f] = 1
        n //= f
        if n in prefact:
            for f in prefact[n]:
                if f in facts: facts[f] += prefact[n][f]
                else: facts[f] = prefact[n][f]
            n = 1
    prefact[origN] = facts
    return facts
def countPrimes(n, p):
    c = 0
    while not n % p:
        c += 1
        n //= p
    return c
def manip(prime, targetMultiplicity):
    currentMultiplicity = 0
    for n in range(targetMultiplicity):
        val = prime * (n+1)
        c = countPrimes(val, prime)
        currentMultiplicity += c
        if targetMultiplicity <= currentMultiplicity: return val
##def manip(p, m): # Prime and multiplicity 
##    adj = m
##    print('m p m/p',m,p,m/p)
##    for d in range(2,math.ceil(m/p)+1):
##        adj -= (d-1)
##        print(d)
##    return p * adj
def s(n):
    facts = factorize(n)
    return max(manip(f,facts[f]) for f in facts)
def S(n):
    return sum(s(n) for n in range(2, n+1))

start = time.perf_counter()
print(S(10**6), time.perf_counter()-start)
# Check these
assert s(2**1) == 2
assert s(2**2) == 4
assert s(2**3) == 4
assert s(2**4) == 6
assert s(2**5) == 8
assert s(2**6) == 8
assert s(2**7) == 8
assert s(5**7) == 30
