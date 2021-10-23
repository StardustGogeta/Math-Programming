import math, time, matplotlib.pyplot as plt, numpy, functools

# The solution is 75737353,
# and it took 102.2976252 seconds to compute with version 5!

# After improving with version 7,
# it takes only 37.6414667 seconds to compute!

def getFactor(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if not n % i:
            return i
    return n

def factorize(n):
    numlist = {1}
    while n - 1:
        f = getFactor(n)
        n //= f
        numlist.update([f * x for x in numlist])
    return sorted(numlist)

def naiveStealthy(n):
    f = factorize(n)[::-1] # O(sqrt(n))
    for i_a in range(len(f) - 1):
        a = f[i_a]
        b = n // a
        for i_c in range(len(f) - 1):
            c = f[i_c]
            d = n // c
            if a + b == c + d + 1: # O(|f|^2) = O(sqrt(n)^2) = O(n)
##                if a < c:
##                    print(a, b, c, d, n)
                return True
    return False

def naiveCountStealthy(N):
    return sum(naiveStealthy(n) for n in range(1, N)) # O(N^2)

def mixedParity(a, b):
    return (a & 1) ^ (b & 1)

def impNaiveStealthy(n):
    f = factorize(n)[::-1] # O(sqrt(n))
    for i_a in range(len(f) - 1):
        a = f[i_a]
        b = n // a
        i_b = f.index(b)

        for i_c in range(i_a + 1, i_b):
            c = f[i_c]
            d = n // c
            if a + b == c + d + 1: # O(|f|^2) = O(sqrt(n)^2) = O(n)
##                if a < c:
##                print(a, b, c, d, n, math.sqrt(n))
                return True
    return False

def impNaiveCountStealthy(N):
    return sum(impNaiveStealthy(n) for n in range(4, N, 4)) # O(N^2)

def imp2NaiveStealthy(n):
    f = factorize(n)[::-1] # O(sqrt(n))
    halfLen = len(f) // 2
    for i_a in range(halfLen):
        a = f[i_a]
        b = n // a

        for i_c in range(i_a + 1, halfLen + 1):
            c = f[i_c]
            # x = a - c = y + 1 = d - b + 1 -> d = a + b - c - 1
            if (a + b - c - 1) * c == n: # O(|f|^2) = O(sqrt(n)^2) = O(n)
##                if a < c:
##                print(a, b, c, d, n, math.sqrt(n))
                return True
    return False

def imp2NaiveCountStealthy(N):
    return sum(imp2NaiveStealthy(n) for n in range(4, N, 4)) # O(N^2)

def imp3NaiveStealthy(n):
    f = factorize(n) # O(sqrt(n))
    L = len(f)
    n4 = n * 4
    for i_b in range(L // 2):
        b = f[i_b]
        a = f[L - i_b - 1]
        m = a + b - 1
        try:
            radicand = m*m - n4
            # We see that c = (m + sqrt(radicand)) / 2 and d = (m - sqrt(radicand)) / 2
            if not math.sqrt(radicand) % 1: # O(sqrt(n))
                return True
        except:
            # Negative radicand, just ignore
            pass
    return False

def imp3NaiveCountStealthy(N):
    return sum(imp3NaiveStealthy(n) for n in range(4, N, 4)) # O(N*sqrt(N))

def imp4NaiveStealthy(n):
    factorSums = set()
    f = factorize(n) # O(sqrt(n))
    L = len(f)
    for i_b in range(L // 2, -1, -1):
        b = f[i_b]
        a = f[L - i_b - 1]
        s = a + b
        if s + 1 in factorSums or s - 1 in factorSums:
##            print(n // 4, n, a, b, conditions(n // 4))
            return True
        factorSums.add(s)
    return False

def imp4NaiveCountStealthy(N):
    return sum(imp4NaiveStealthy(n) for n in range(4, N, 4)) # O(N*sqrt(N))

def imp5NaiveCountStealthy(N): # THIS ONE WORKED!
    # Each stealthy number n corresponds exactly to one product of triangular numbers equal to n/4
    # TRI_PRODUCTS generation takes O(sqrt(N)^2) = O(N) time
##    return sum(imp5NaiveStealthy(n) for n in range(4, N, 4)) # O(N)
    N4 = N // 4
    return len([t for t in TRI_PRODUCTS if t <= N4])

@functools.lru_cache(10**7)
def imp6CountStealthy(N): # BROKEN
    ret = 0
    for T in sorted(TRIANGULARS): # O(sqrt(N))
        if T < N:
##            i = countTriangularsTo(N // T)
            potentialProds = countTriangularsTo(N // T) # O(1)
##            print(N, T, i, potentialProds)
            ret += potentialProds
    ##        print(ret)
    return ret # O(sqrt(N))

def imp7CountStealthy(N):
    N4 = N // 4
    ret = set()
    ls = sorted(TRIANGULARS)
    for i in range(len(ls)):
        for j in range(i, len(ls)):
            to_add = ls[i] * ls[j]
            if to_add <= N4:
                ret.add(to_add)
            else:
                break
    return len(ret)

def genTriangulars(N):
    ret = set()
    x = 1
    inc = 2
    while x < N:
        ret.add(x)
        x += inc
        inc += 1
    return ret

def countTriangularsTo(N):
    return int(math.sqrt(1 + 8 * N) - 1) // 2

def products(ls, T_index = 6):
##    T = sorted(TRIANGULARS)[T_index]
##    origs = dict()
##    colls = set()
    ret = set()
    for i in range(len(ls)):
        for j in range(i, len(ls)):
            to_add = ls[i] * ls[j]
            if to_add <= N: # THIS WAS THE CRUCIAL INGREDIENT!
##                if to_add in ret:
##                    orig_i, orig_j = origs[to_add]
##                    if T in [ls[i], ls[j], orig_i, orig_j]:
##                        colls.add((to_add, ls[i], ls[j], orig_i, orig_j))
##                        print("COLLISION: ", to_add)
##                else:
##                    origs[to_add] = (ls[i], ls[j])
                ret.add(to_add)
            else:
                break
##    print(f"{T_index} : \t{T}\tCOLLISIONS --", len(colls), len(factorize(T)))
##    for c, i, j, orig_i, orig_j in sorted(colls):
##        print(c, i, j, orig_i, orig_j)
    return ret

N = 10**14

##start = time.perf_counter()
##ls = naiveCountStealthy(N)
##end = time.perf_counter()
##print(end - start)

##start = time.perf_counter()
##ls2 = imp2NaiveCountStealthy(N)
##end = time.perf_counter()
##print(end - start)

##start = time.perf_counter()
##ls3 = imp3NaiveCountStealthy(N)
##end = time.perf_counter()
##print(end - start)
##print(ls3)

def conditions(n):
    ret = []
##    n_T = (math.sqrt(1 + 8 * n) - 1) // 2
##    if n_T * (n_T + 1) // 2 == n:
##        ret.append("triangular")
##        n_T = (math.sqrt(1 + 8 * n) - 1) // 2
##    if not n % 10:
##        n_T10 = (math.sqrt(1 + 8 * n // 10) - 1) // 2
##        if n_T10 * (n_T10 + 1) // 2 == n // 10:
##            ret.append("10x triangular")
##    if not n % 9:
##        ret.append("mult9")
##    if not n % 3:
##        ret.append("mult3")
##    if n in TRIANGULARS:
##        ret.append("triangular")
    if n in TRI_PRODUCTS:
        ret.append("triproduct")
    return ", ".join(ret)

##start = time.perf_counter()
##ls4 = imp4NaiveCountStealthy(N)
####tri4 = (math.sqrt(1 + 2 * N) - 1) // 2
##end = time.perf_counter()
##print(end - start)
##print(ls4, tri4, tri4 / ls4)
##
##start = time.perf_counter()
##ls4 = imp4NaiveCountStealthy(10*N)
##end = time.perf_counter()
##print(end - start)
##print(ls4)
##print(ls3, ls4)

start = time.perf_counter()
TRIANGULARS = genTriangulars(N // 4) # O(sqrt(N)) time
##for i in range(len(TRIANGULARS)):
##    print("i : ", i)
##    TRI_PRODUCTS = products(list(TRIANGULARS), i) # O(sqrt(N)^2) = O(N) time

##TRI_PRODUCTS = products(sorted(TRIANGULARS)) # O(sqrt(N)^2) = O(N) time
##ls5 = imp5NaiveCountStealthy(N) # O(N) time

ls7 = imp7CountStealthy(N)

end = time.perf_counter()
print(end - start)
print(ls7)

##start = time.perf_counter()
##TRIANGULARS = genTriangulars(N // 4) # O(sqrt(N)) time
##ls6 = imp6CountStealthy(N) # O(sqrt(N)) time
##end = time.perf_counter()
##print(end - start)
##print(ls5, ls6)

##xs = []
##for mag in range(3, 6):
##    for mult in range(1, 10, 2):
##        xs.append(mult * 10 ** mag)
##ys = [imp3NaiveCountStealthy(x) for x in xs]
##
##def log(xs):
##    return [math.log(x) for x in xs]
##
##plyft = numpy.polyfit(log(xs), log(ys), 1)
##print(plyft)
##
##fs = [x**plyft[0] * math.exp(plyft[1]) for x in xs]
##
####plt.scatter(log(xs), log(ys))
##plt.scatter(xs, ys)
##plt.plot(xs, fs)
##plt.show()

##ts = list(range(1,10**3))
##stealthy = [t*imp4NaiveStealthy(t) for t in ts]
##plt.scatter(ts, stealthy)
##plt.show()


##last = 0
##for x in range(2, N):
##    if imp2NaiveStealthy(x):
##        print(f"{x}\t{x % 4}\t{x%8}\t{x%12}\t{x%16}\t{x-last}")
##        last = x

# ----- Trying a multilinear regression to detect some pattern I don't see -----

# INPUTS:
# pi function (prime count), number of divisors, remainder modulo 4, 8, 12?

# OUTPUTS:
# stealthy count








