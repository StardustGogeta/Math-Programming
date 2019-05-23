from decimal import *
import math

def convert(n):
    getcontext().prec = math.ceil(math.log10(n))
    numlist=[1]
    while n-1:
            f = int(findFactor(n))
            n /= f
            numlist+=[f*x for x in numlist]
            numlist=list(set(numlist))
    numlist.sort()
    return(numlist)

def findFactor(n):
    for d in range(2, math.ceil(Decimal(n).sqrt())):
        if (n % d == 0):
            return(d)
    return(n)

#getcontext().prec = 500
#convert(Decimal(input("What is the number?\n")))
