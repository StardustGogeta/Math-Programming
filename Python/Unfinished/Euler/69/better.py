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
ratios = [n/totient(n) for n in range(2,1000000)]
maxI = ratios.index(max(ratios))
print(maxI+2, ratios[maxI])
print(time.perf_counter()-start)
