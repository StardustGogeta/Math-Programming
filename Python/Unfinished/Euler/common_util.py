
# Uses the Sieve of Eratosthenes to find all prime numbers up to N
def efficientSieve(N):
    allNums = list(range(2, N + 1))
    primes = []
    for i in range(len(allNums)):
        n = allNums[i]
        if n:
            for j in range(i+n, len(allNums), n):
                allNums[j] = 0
    return list(filter(lambda x: x, allNums))

