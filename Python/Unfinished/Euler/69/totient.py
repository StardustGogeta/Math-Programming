import math, time
def factors(n):
    f = set()
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d:
            f.add(n//d)
            f.add(d)
    return f

def phi(n):
    facts = factors(n)
    #print(n, facts)
    c = 0
    for x in range(1, n):
        if x not in facts and math.gcd(n, x) == 1:
            c += 1
            #print(x,c)
    return c

start = time.perf_counter()
vals = [n/phi(n) for n in range(2, 10**4+1)]
print(vals.index(max(vals))+2, time.perf_counter()-start)
