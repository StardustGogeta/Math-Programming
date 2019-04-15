import math
S= [290797]
last = S[-1]
for n in range(1, 10**7+1):
    new = last**2 % 50515093
    S.append(new)
    last = new
print("FINISHED S") # Finishes quickly enough, no modification needed

def T(n, p): return S[n] % p # O(1), but slows things down

def N(p, q): # O(q) complexity, n is about p ** q for very large q
    return sum(T(n, p) * p**n for n in range(0, q+1))

def NF(p, q):
    n = N(p, q) # O(q) complexity
    print("FINISHED N") # N is too slow at the required input
    ret = 0
    # The following loop takes care of the Nfac behavior by looking for where all the factors would be / could be
    for m in range(1, int(1+math.log(n)//math.log(p))): # O(log(n)) complexity, about O(q) for very large q
        # Better than the naive approach that is O(n), or about O(p^q) for very large q (terrible!)
        # Enables test cases to be performed off which to improve
        ret += n // (p ** m)
    return ret
