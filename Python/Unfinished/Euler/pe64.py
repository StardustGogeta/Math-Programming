from math import sqrt, floor
import time
def period(n):
    s = int(sqrt(n))
    if s**2 == n: return 0
    a = [s]
    b = s
    num = 1
    x = -2
    visited = []
    while 1:
        x += 1
        if (a, num, b) in visited: return x
        visited += [(a, num, b)]
        num = (n - b**2) // num
        newA = (s - b) // num
        b = -b - newA * num

s = time.perf_counter()
c = 0
for n in range(1, 10001):
    if period(n) % 2: c += 1
print(c)
print(time.perf_counter()-s)
