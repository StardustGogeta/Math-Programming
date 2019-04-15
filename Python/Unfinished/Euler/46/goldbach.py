import math

def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True

def composite(n): return not prime(n)

sqrt2 = 2**.5
for n in range(1, 10**4, 2):
    if composite(n):
        truthy = False
        for sqrt in range(math.floor(math.sqrt(n)/sqrt2)+1):
            if prime(n-2*sqrt**2):
                truthy = True
                break
        if not truthy:
            print(n)
            break

