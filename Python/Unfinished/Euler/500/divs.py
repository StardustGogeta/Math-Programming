import math

#def prime(n):
#    for d in range(2, math.floor(math.sqrt(n))+1):
#        if not n % d: return False
#    return True

#def divisorCount(n):
#    if n < 2: return 1
#    if prime(n): return 2
#    return sum(divisorCount(d)+divisorCount(n//d) for d in range(2, math.floor(math.sqrt(n))+1) if not n % d)**2

####def divisorCount(n):
####    return sum(n//k-(n-1)//k for k in range(1, n+1))

##def divisorCount(n):
##    c = 0
##    for d in range(1, math.floor(math.sqrt(n))+1):
##        if not n % d: c += 2
##    if not math.sqrt(n) % 1: c -= 1
##    return c

for x in range(1, 20):print(x,":",divisorCount(x))
m = 1
for x in range(1, 20):
    print(m,":",divisorCount(m))
    m *= x
