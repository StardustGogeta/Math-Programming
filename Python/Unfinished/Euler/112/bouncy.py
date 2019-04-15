import math

def bouncy(n):
    s = str(n)
    up = False
    down = False
    for e in range(len(s)-1):
        if int(s[e]) < int(s[e+1]): up = True
        elif int(s[e]) > int(s[e+1]): down = True
    return up and down

b = 0
for x in range(100,10**8):
    if bouncy(x): b += 1
    if not x % 10**6: print(b / x)
    if b / x == .99:
        print(x)
        break
