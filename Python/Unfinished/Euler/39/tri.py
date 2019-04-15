# This solution is O(n^2) and needs a lot of work to fix.

# All Pythagorean triples are of the form (a, (a^2-p^2)/2p, (a^2+p^2)/2p)
import math
#baseLengths = set()
perims = dict()
# This is the point where b <= a
sqrt2_1 = math.sqrt(2)-1
for a in range(2, 1001):
    a2 = a**2
    for p in range(2-(a%2), int(a*sqrt2_1+1), 2):
        p2 = p**2
        if not (a2-p2) % (2*p):
            perim = (a + a2/p)
            if perim <= 1000:
                if perim in perims:
                    perims[perim] += 1
                else:
                    perims[perim] = 1
M = max(perims.values())
for p in perims:
    if perims[p] == M:
        print(p)
        break
