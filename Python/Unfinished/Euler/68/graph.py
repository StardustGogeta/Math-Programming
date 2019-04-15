# Problem 68
# This solution is O(n!), but n is only 10 so it is fine
import itertools

def ringString(chain):
    minBranch = min(map(int, chain[0::2]))
    minInd = chain.index(str(minBranch))
    branchSum = int(chain[0])+int(chain[1])+int(chain[3])
    string = ''
    for i in range(minInd, minInd+len(chain), 2):
        circ = i % len(chain)
        if int(chain[circ]) + int(chain[circ+1]) + int(chain[(circ+3) % len(chain)]) == branchSum:
            string += chain[circ]+chain[circ+1]+chain[(circ+3) % len(chain)]
        else:
            return 0
    return int(string)

cells = list(map(str, range(1, 11)))
M = 0
for perm in itertools.permutations(cells):
    R = ringString(perm)
    if R < 10**16:
        M = max(ringString(perm), M)
print(M)
