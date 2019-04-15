"""
Here's my approach: Label the three points A, B, and C. The acceptable region for C can then be found using only points A and B.
First, construct a ray to point A from the origin, and reflect this ray over the origin. Repeat for point B.
From here, in order for the triangle formed to contain the origin, C can only be located between these two reflected rays.
"""
import numpy as np
from math import pi
import time

def reflect(a):
    if a >= 0:
        return a - pi
    if a < 0:
        return a + pi
def withinRange(a, a2, c):
    if abs(a2 - a) < pi:
        a, a2 = min(a, a2), max(a, a2)
    else:
        a2, a = min(a, a2), max(a, a2)
    b = reflect(a)
    b2 = reflect(a2)
    return b2 > c > b
def angleTo(pt):
    angle = np.angle(pt[0]+pt[1]*1.0j)
    return angle

##A, B, C = (-340, 495), (-153, -910), (835, -947)
##a, b, c = angleTo(A), angleTo(B), angleTo(C)
###X, Y, Z = (-175, 41), (-421, -714), (574, -645)
##X, Y, Z = (-547,712),(-352,579),(951,-786)
##x, y, z = angleTo(X), angleTo(Y), angleTo(Z)
##print(a,b,c,withinRange(a,b,c), withinRange(b,c,a), withinRange(c,a,b))
##print(x,y,z,withinRange(x,y,z), withinRange(y,z,x), withinRange(z,x,y))
##D, E, F = (-1, -1), (2,1), (-1,1)
##d, e, f = angleTo(D), angleTo(E), angleTo(F)
##print(d,e,f,withinRange(d,e,f), withinRange(e, f, d), withinRange(f, d, e))
data = open('p102_triangles.txt')
nums = [int(x) for line in data.read().splitlines() for x in line.split(',')]
data.close()
valid = 0
#print(len(nums))
for i in range(len(nums)//6):
    a, b, c, d, e, f = nums[i*6:i*6+6]
    A, B, C = (a,b), (c,d), (e,f)
    a, b, c = angleTo(A), angleTo(B), angleTo(C)
    #print(withinRange(a,b,c) or withinRange(b,c,a))
    valid += (withinRange(a,b,c) or withinRange(b,c,a))
print(valid)
