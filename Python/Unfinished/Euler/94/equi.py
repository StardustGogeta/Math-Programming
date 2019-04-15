# Naive approach with Heron's formula
import math, time
##def heron(a, b, c):
##    s = (a+b+c)/2
##    return math.sqrt(s*(s-a)*(s-b)*(s-c))
##
##summation = 0
##for S in range(1,(10**9)//3+1):
##    if not heron(S, S, S-1) :
##        summation += 3*S-1
##    if not heron(S, S, S+1):
##        summation += 3*S+1

# Note: The only isosceles triangles with integer area are those where S is the hypotenuse in a Pythagorean triple and the other side is two times one of the legs
start = time.perf_counter()
summation = 0
for S in range(1,(10**9)//3+1):
    S2 = S**2
    if not math.sqrt(S2-((S-1)/2)**2) % 1:
        summation += 3*S-1
    if not math.sqrt(S2-((S+1)/2)**2) % 1:
        summation += 3*S+1
print(summation, time.perf_counter()-start)
