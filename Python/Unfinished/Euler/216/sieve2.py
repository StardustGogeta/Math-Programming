import math, time
# Don't even bother running this unless major optimizations are made;
# efficientSieve on the order of N > 10^8 kills the computer temporarily
def efficientSieve(N):
    allNums = list(range(2, N))
    primes = []
    for i in range(len(allNums)):
        n = allNums[i]
        if n:
            for j in range(i+n, len(allNums), n):
                allNums[j] = 0
    return set(filter(lambda x: x, allNums))

def smallestFactors(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return (d, n//d)

primes = efficientSieve(2*(10**2)**2)
print("yay")

def t(n):
    return 2*n**2-1

p = 0
for n in range(2, 10**2):
    T = t(n)
    if T in primes:
        p += 1
    else:
        pass #print(n, smallestFactors(T))
print(p)
