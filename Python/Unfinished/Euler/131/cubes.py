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

# Quadratic for n was solved by hand,
# then it was observed that m, for some reason, consists only of perfect squares n**(2/3)
# and n is always a perfect cube m**(3/2) if and only if p is valid
def validP(p):
    for sqrtm in range(1, math.ceil(math.sqrt(p//3))):
        m = sqrtm**2
        #print(m)
        if not (3*m**2+math.sqrt(9*m**4+4*m**3*(p-3*m))) % (2*(p-3*m)):
            #print(p, m, (3*m**2+math.sqrt(9*m**4+4*m**3*(p-3*m)))//(2*(p-3*m)))
            return True
    return False

primes = efficientSieve(10**6)
print("primed", len(primes))
print(len(list(filter(validP, primes))))

