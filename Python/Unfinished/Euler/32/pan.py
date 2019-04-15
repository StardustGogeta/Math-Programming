import math

def findPandigitalsWithProduct(n):
    s = str(n)
    chars = set("123456789")
    for d in range(2, math.floor(math.sqrt(n))):
        if not n%d:
            combinedStr = s+str(d)+str(n//d)
            if len(combinedStr) == 9 and set(combinedStr) == chars:
                #print(n, '=', d, '*', n//d, set(s+str(d)+str(n//d)))
                return n
    return 0

# 99*999 is a rough estimate for the upper bound of the product, rounded up to 100000
print(sum(findPandigitalsWithProduct(x) for x in range(100000)))
