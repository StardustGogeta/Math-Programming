# O(n^2), would take 21.238 years to execute
import math, time
start = time.perf_counter()
##count = 0
##for n in range(1,10**3):
##    xs = 0
##    for a in range(math.ceil(math.sqrt(n/3)),n+1):
##        d = (n+a**2)/(4*a)
##        if (not d % 1) and a/4 < d < a:
##            #print(a, n, 2*n, d)
##            xs += 1
##    if xs == 1:
##        count += 1
##        #print(n)
##print("COUNT:",count, time.perf_counter()-start)
n_counts = dict()
threshold = 10**3
for a in range(1, threshold):
    for d in range(math.ceil(a/4), a):
        n = a*(4*d-a)
        if n in n_counts:
            n_counts[n] += 1
        else:
            n_counts[n] = 1
s = 0
for n in n_counts:
    if n < threshold and n_counts[n] == 1:
        #print(n)
        s += 1
print(s, time.perf_counter()-start)
