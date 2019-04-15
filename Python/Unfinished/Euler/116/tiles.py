# n is the total number of tiles, counted in black units
# x is the number of colored tiles to be inserted
# c is the color (0 for red, 1 for green, 2 for blue)

# Test Cases
# newParts(3,2) -> 4
# newParts(1,3) -> 3
# newParts(2,2) -> 3
# newParts(1,2) -> 2
# newParts(4,2) -> 5
# newParts(2,3) -> 6
cache = dict()
def newParts(n, k): # By investigation
    if (n, k) in cache: return cache[(n,k)] # Major speedup
    if k == 1: return 1 # A single pile has only one partition
    s = sum(newParts(n-i, k-1) for i in range(n+1)) # Move one colored to the left,
    # and iterate through all possible combos of blacks to its left and right
    # (Very similar to restricted partitions problem)
    cache[(n,k)] = s
    return s

def multiColor(c, x, n):
    return newParts(n-x*(c+2), x+1)

def totalColor(c, n):
    return sum(multiColor(c, x, n) for x in range(1, n//(c+2)+1))

def total(n):
    return sum(totalColor(c, n) for c in range(3))
