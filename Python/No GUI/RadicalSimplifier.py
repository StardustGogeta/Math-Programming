import math

def findFactor(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if (n % d == 0):
            return(d)
    return(int(n))

rad = int(input("What is the number inside the radical?\n"))
exp = int(input("What is the number outside the radical?\n"))
a = round(rad**(1/exp),12)
if a % 1 == 0:
    print("Your value is {0}.".format(a))
else:
    factors = []
    o = rad
    out = 1
    while rad > 1:
        n = findFactor(rad)
        factors.extend([n])
        rad /= n
    for x in factors:
        if factors.count(x) >= exp:
            for _ in range(exp):
                A = factors.index(x)
                factors.pop(A)
            out *= x
    print("{0} \u221a {1}".format(out,int(o/out**exp)))
        
    
