import sympy
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
x = 0
for n in range(1, 101):
    r = 1
    while sympy.binomial(n,r) <= 10**6 and r < n: r+= 1
    if r >= n: continue
    x += (((n+1) // 2) - r) * 2 + (n+1) % 2
print(x)
