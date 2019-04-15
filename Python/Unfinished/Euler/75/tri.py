# This solution is O(n^2) and needs a lot of work to fix.

# All Pythagorean triples are of the form (a, (a^2-p^2)/2p, (a^2+p^2)/2p)
import math, time
#baseLengths = set()
possibles = set()
duplicates = set()
L = 10000
# This is the point where b <= a
sqrt2_1 = math.sqrt(2)-1
start = time.clock()
for a in range(2, L//3):
    a2 = a**2
    for p in range(2-(a%2), int(a*sqrt2_1+1), 2):
        p2 = p**2
        if not (a2-p2) % (2*p):
            toAdd = (a + a2/p)
            if toAdd <= L:
                if toAdd in possibles: duplicates.add(toAdd)
                else: possibles.add(toAdd)
print(len(possibles-duplicates))
print(time.clock()-start)
