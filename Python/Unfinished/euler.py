import math

def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def is_prime(x):
    return all(x%d for d in range(2, 1+math.floor(math.sqrt(x))))

# __________________________

def pe33():
    for x in range(10,100):
        for y in range(x+1,100):
            a, b = str(x), str(y)
            if a[0] in b:
                if a[0] == b[0]:
                    if int(a[1])/int(b[1]) == x/y:
                        print(x,y)
                else:
                    if int(a[1])/int(b[0]) == x/y:
                        print(x,y)
            elif a[1] in b and a[1] != '0':
                if a[1] == b[0] and b[1] != '0':
                    if int(a[0])/int(b[1]) == x/y:
                        print(x,y)
                else:
                    if int(a[0])/int(b[0]) == x/y:
                        print(x,y)
                

def pe35():
    derp = 0
    for x in range(2,10**6):
        X = str(x)*2
        L = len(X)//2
        bad = False
        for n in range(L):
            num = int(X[n:n+L])
            if not is_prime(num):
                bad = True
        if not bad:
            derp += 1
    return derp

##def pe493():
##    f = math.factorial
##    E = 0
##    E += 0 * (f(50)/f(30)) / (f(70)/f(50)) * choose(70,0)
##    E += 1 * 
##    pass

def pe587():
    A = 0
    res = 10000000
    slope = 1/2239
    for rect in range(res):
        x = rect/res
        y = min(slope*x,1-math.sqrt(2*x-x**2))
        #print(slope*x,1-(2*x-x**2)**.5)
        A += y
    return A/(1-math.pi/4)/res
