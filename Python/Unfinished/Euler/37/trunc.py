import math

def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n%d: return False
    return n > 1

def truncatablePrime(n):
    s = str(n)
    for x in range(1, len(s)):
        if not prime(int(s[:x])): return False
    for x in range(0, len(s)):
        #print(s, x, int(s[x:]))
        if not prime(int(s[x:])): return False
    print(n)
    return n

print("Sum:", sum(truncatablePrime(x) for x in range(10,1000000)))
# 3797, 379, 79, 797

# 373, 73
