b = False
M = 0
for n in range(999, 99, -1):
    for m in range(999, n-1, -1):
        x = n*m
        if x < M: break
        s = str(n*m)
        if s[::1] == s[::-1]:
            M = x
            break
print(M)
