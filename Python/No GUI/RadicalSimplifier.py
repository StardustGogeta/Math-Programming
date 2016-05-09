from math import sqrt, floor
def f(n):
    for d in range(2, floor(sqrt(n))+1):
        if not n%d: return d
    return int(n)
def e(a,b,c,d,e):
    return (a*c**(d//e),b*c**(d%e))
r = int(input("What is the number inside the radical?\n"))
x = int(input("What is the root?\n"))
a = round(r**(1/x),12)
if not a%1:
    print("Your value is {0}.".format(int(a)))
else:
    i,o,fV,fC = [1]*4
    while r > 1:
        n = f(r)
        if fV == n: fC += 1
        else: fC,fV,(o,i) = 1,n,e(o,i,fV,fC,x)
        r /= n
    print("Your value is {0} {2}√{1}.".format(*e(o,i,fV,fC,x),''.join([['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹'][int(y)] for y in str(x)])))
