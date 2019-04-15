import math
from decimal import *
getcontext().prec = 32

p_values = {}

# Using the following sources:
# https://en.wikipedia.org/wiki/Divisor_function
# https://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function
# https://mathoverflow.net/questions/127000/partitions-sum-of-divisors-identity
# https://en.wikipedia.org/wiki/Arithmetic_function

# TODO: Rewrite with pentagonal numbers: https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function

def sumOfDivisors(n):
    if n == 1: return 1
    s = 0
    for d in range(1, math.floor(Decimal(n).sqrt()+1)):
        if not n % d:
            s += d
            if d != n//d : s += n//d
    return s

def p(n):
    if n == 0: return 1
    if n in p_values: return p_values[n]
    #P = 1/Decimal(n) * sum(sumOfDivisors(n-k) * Decimal(p(k)) for k in range(0,n))
    P = 0
    for k in range(0, n):
        P += sumOfDivisors(n-k) * p(k)
        #if n == 115: print(P, k)
    P //= n
    #print(P)
    p_values[n] = P
    return P

##X = 1
##while p(X) % 10**6:
##    X += 1
##    if X == 1000: print("success!",p(X))
##print(X)
##1 1 1 1 1
##1 1 1 2
##1 2 2
##1 1 3
##1 4
##5
##2 3
