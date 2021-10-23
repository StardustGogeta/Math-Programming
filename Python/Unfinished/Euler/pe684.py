import math, time, functools

M = 1000000007

# We see that s(n) looks like 19, 29, 39, etc.
# The sum is given easily via summation.

# For S(20), we get the following sum:
#   0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
# + 9 + 19 + 29 + 39 + 49 + 59 + 69 + 79 + 89
# + 99 + 199 + 299 => 100 + 200 + 300 - 3 = 597 = sum(1, r + 1) * 10^q - (r + 1)

@functools.lru_cache()
def f(i):
    if i < 2:
        return i
    return f(i-1) + f(i-2)

def S(k):
    q, r = divmod(k, 9)
##    q = k // 9
##    r = k % 9
    # 45 * (1-10**(N+1))/(1-10)
    mainSum = 5 * (pow(10, q, M) - 1) - 9 * q
    remSum = (r + 2) * (r + 1) // 2 * pow(10, q, M) - (r + 1)
##    print(mainSum, remSum)
    return mainSum + remSum

val = 0
for i in range(2, 91):
##    print("i", i)
    val += S(f(i))
    val %= M
print(val)
