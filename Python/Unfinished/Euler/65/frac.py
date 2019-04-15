from fractions import Fraction

arr = [x for y in [(1,2*k,1) for k in range(40)] for x in y]
N = 100
k = Fraction(arr[N+1])
for n in range(N, -1, -1):
    k = 1/k + arr[n]
print(k)
print(sum(int(c) for c in str(k).split('/')[0]))
