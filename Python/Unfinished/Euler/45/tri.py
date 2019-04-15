import math

def T(n):
    return n*(n+1)/2

# The quadratic formula gives:
# n_P = (1/2+sqrt(1/4+6T))/3
# n_H = (1+sqrt(1+8T))/4
t = 286
while 1:
    tVal = T(t)
    if not (1/2+math.sqrt(1/4+6*tVal))/3 % 1:
        if not (1+math.sqrt(1+8*tVal))/4 % 1:
            print(t, tVal)
            break
    t += 1
