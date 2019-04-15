import math
from decimal import *
getcontext().prec = 25

# Using Diophantine solver at https://www.alpertron.com.ar/JQUAD.HTM
# with 2, 0, -1, 0, 0, 2

# If a(a-1)/(b(b-1)) = 1/2, then b^2-b-2a^2+2a = 0 and b=(1+sqrt(1+8a^2-8a))/2
# Then, the radicand is a perfect square, and a=(2+sqrt(2+2n^2))/4 for integer n
# The radicand, again, is a perfect square, so 2+2n^2-m^2 = 0 for integers n,m

x = 1
y = 2
for _ in range(20):
    newX = 3*x+2*y
    newY = 4*x+3*y
    x,y=newX,newY
    print(x, y, "test:", 2+2*x**2-y**2)
    n = x
    a = (2+math.sqrt(2+2*n**2))//4
    b = (1+math.sqrt(1+8*a**2-8*a))//2
    print("Solution:",a, b)
    if b > 10**12: break
