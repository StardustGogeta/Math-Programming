def pentagonal(n):
    return n*(3*n-1)//2

def isPentagonal(S):
    sq = (1+24*S)**.5
    #if sq % 1: return False
    return (1+sq)/6 % 1 == 0

###pentas = list(map(pentagonal, range(1, 10**3)))
##for u in range(-100000, 0):
### With a test bound of -100000, it is shown that 285991995532
###   is the lowest difference for consecutive pentagonals
##    # The difference between pentagonals P(n+1)-P(n) is (3n+1)
##    # This is the integer solution set of consecutive differences that are pentagonals
##    x = 18*u**2+13*u+2
##    y = -6*u-2
##    #print(6*x+2-3*y**2+y)
##    X = pentagonal(x+1)
##    Y = pentagonal(x)
##    if isPentagonal(X+Y): print(x,y, pentagonal(y), pentagonal(x), pentagonal(x+1))

for n in range(1, 4000):
    N = pentagonal(n)
    for m in range(1, n):
        M = pentagonal(m)
        if isPentagonal(N-M) and isPentagonal(N+M):
            print(N-M)
