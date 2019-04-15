import itertools
# https://en.wikipedia.org/wiki/Polygonal_number
def P(s, n): # Return the nth polygonal number with s sides
    return n*(n-1)*(s-2)//2+n
def invP(s, x): # Find if x is a polygonal number with s sides
    return ((8*(s-2)*x+(s-4)**2)**.5+(s-4))//(2*s-4) % 1 == 0

def getValidPoly(s):
    x, n = 1, 1
    while x < 1000:
        n += 1
        x = P(s, n)
    ret = []
    while 1:
        n += 1
        x = P(s, n)
        if x < 10000: ret += [x]
        else: break
    return list(filter(lambda n: str(n)[2]!='0', ret)) # Remove all 4-digit numbers where the third digit is zero

poly3 = getValidPoly(3)
poly4 = getValidPoly(4)
poly5 = getValidPoly(5)
poly6 = getValidPoly(6)
poly7 = getValidPoly(7)
poly8 = getValidPoly(8)

polys = [poly3, poly4, poly5, poly6, poly7, poly8]
paths = itertools.permutations(range(6))

for path in paths:
    for p0 in polys[path[0]]:
        end0 = str(p0)[2:]
        for p1 in list(filter(lambda x: str(x).startswith(end0), polys[path[1]])):
            end1 = str(p1)[2:]
            for p2 in list(filter(lambda x: str(x).startswith(end1), polys[path[2]])):
                end2 = str(p2)[2:]
                for p3 in list(filter(lambda x: str(x).startswith(end2), polys[path[3]])):
                    end3 = str(p3)[2:]
                    for p4 in list(filter(lambda x: str(x).startswith(end3), polys[path[4]])):
                        end4 = str(p4)[2:]
                        for p5 in list(filter(lambda x: str(x).startswith(end4), polys[path[5]])):
                            if str(p5)[2:]==str(p0)[:2]: print(p0, p1, p2, p3, p4, p5, path, p0+p1+p2+p3+p4+p5)
