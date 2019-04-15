import math
def efficientSieve(N):
    allNums = list(range(2, N))
    primes = []
    for i in range(len(allNums)):
        n = allNums[i]
        if n:
            for j in range(i+n, len(allNums), n):
                allNums[j] = 0
    return list(filter(lambda x: x, allNums))

def S(p1, p2):
    pre = 0
    L = len(str(p1))
    mod = p1-p2
    inc = 10**L % p2
    x = 1
##    while mod % p2:
##        mod += inc
##        pre += 1
####    while 1:
####        toAdd = math.ceil((p2*x-mod)/inc)
####        print(toAdd, x, p1, p2, pre, mod)
####        pre += toAdd
####        mod += toAdd * inc
####        x += 1
####        mod %= p2
####        if not mod: break
    while (p2*x-mod) % inc:
        x += 1
    pre = (p2*x-mod) // inc
    #print(p1, p2, pre, inc, p1, p1 + 10**L * pre)
    # This is a linear Diophantine equation where pre*inc=p2*x-(p1-p2) [solving for pre]
    # This way is faster than string processing, by far
    return p1 + 10**L * pre

primes = efficientSieve(10**6+10**4)
total = 0
for i in range(2, len(primes)-1):
    p1, p2 = primes[i:i+2]
    if p1 > 10**6: break
    total += S(p1, p2)
print(total)
