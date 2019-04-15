import math
def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True

primes = list(filter(prime, range(2,math.ceil(math.sqrt(50*10**6)))))
squares = [p**2 for p in primes if p**2 < 50*10**6]
cubes = [p**3 for p in primes if p**3 < 50*10**6]
fourths = [p**4 for p in primes if p**4 < 50*10**6]
expressibles = set()
for x in squares:
    for y in cubes:
        for z in fourths:
            expressibles.add(x+y+z)

print(sum(n in expressibles for n in range(50*10**6)))
