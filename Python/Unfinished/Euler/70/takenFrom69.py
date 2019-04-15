import math, time
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

start = time.perf_counter()
m = (100, 1)
for n in range(2, 10000000):
    t = totient(n)
    if sorted(str(n)) == sorted(str(t)):
        if n / t < m[0]:
            m = (n / t, n)
print(m[1], m[0])
print(time.perf_counter()-start)
