def rects(n, m):
    return n*(n+1)*m*(m+1)//4

closest = (3*10**6, 0, 0)
for n in range(1, 2000):
    for m in range(1, 2000):
        A = abs(rects(n, m) - 2*10**6)
        if closest[0] > A:
            closest = (A, n, m)
print(closest)
