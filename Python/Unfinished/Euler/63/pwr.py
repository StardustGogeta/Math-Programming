import time

def pwrs(x):
    n = 1
    while len(str(x**n)) == n:
        n += 1
    return n-1

s = time.clock()
# Numbers >= 10 will exceed the required growth rate, and 0 does not count
t = sum(pwrs(x) for x in range(1,10))
print(t, time.clock()-s)
