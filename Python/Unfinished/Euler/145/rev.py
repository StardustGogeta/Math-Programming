# A mostly-brute-force approach [O(n)] with a couple optimizations
import time

# The below function is flawed - It results in an incorrect answer!
def oddEvenEq(s):
    e = 0
    for L in s:
        if L in "02468": e += 1
    return abs(e-len(s)//2) < 2

def oddDigits(x, s):
    return all(c in "13579" for c in str(x+int(s[::-1])))

# Only counting those with even first digits and odd last digits
# Only counting those with equal numbers of odd/even digits
t = time.clock()
threshold = 10**9
n = 0
for x in range(1,threshold,2):
    s = str(x)
    if s[0] in "2468" and oddEvenEq(s) and oddDigits(x, s) and s[-1] != '0':
    #if str(x)[0] in "2468" and set(str(x+int(str(x)[::-1]))) <= set("13579") and str(x)[-1] != '0':
    #if set(str(x+int(str(x)[::-1]))) <= set("13579") and str(x)[-1] != '0':
        n += 2
        #print(x)
print(n, time.clock()-t)
