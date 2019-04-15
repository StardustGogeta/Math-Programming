import math

charSets = [set("123456789"[:L]) for L in range(10)]

def pandigital(n):
    s = str(n)
    chars = charSets[len(s)]
    return set(s) == chars

def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True

# Cannot be digits 1-8 or 1-9 without being divisible by 3
for x in range(10**7-1, 2140, -1):
    if pandigital(x) and prime(x):
        print(x)
        break
