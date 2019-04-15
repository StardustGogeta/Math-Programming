import math
from decimal import *
getcontext().prec = 25
s = Decimal(.5).sqrt()

for x in range(10**12, 2*10**12):
#for x in range(2, 200):
    n = math.ceil(s*x)
    top = Decimal(n-1)*Decimal(n)
    bottom = (Decimal(x)*Decimal(x-1))
    ratio = top/bottom
    if ratio == Decimal(.5):
        print(x,n)
