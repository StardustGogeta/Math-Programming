import math, time
def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True
def stmtTrue(a,n):
    return a*(a-1) % n == 0

def M(n):
    if prime(n): return 1 # This seems to be a very slight optimization
    # Something is broken here!
    #print(n)
    for a in range(n-1, math.floor(math.sqrt(n))-1, -1):
        if stmtTrue(a, n): return a
    return 1

def m(n):
    if prime(n): return 1 # This seems to be a very slight optimization
    for a in range(math.floor(math.sqrt(n)),n):
        if stmtTrue(a, n): return a-1
    return 1

def optimizedM(n):
    mVal = m(n)
    if mVal == 1: return 1
    else: return n - mVal

#print(M(6))

# 4 (n=6) has 7 nums between its repetitions up to 12
# 6 (n=10) has 11 nums between its repetitions up to 30
start = time.perf_counter()
print(sum(optimizedM(n) for n in range(2,10**4+1)))

# Helps for finding patterns!
##for n in range(201):
##    print('n:',n,'\tM(n):',M(n),'\tm(n):',m(n),'\tSum:',m(n)+M(n)-1)#,'\t',(not prime(n) or (prime(n) and M(n)==1)))

print(time.perf_counter()-start)
