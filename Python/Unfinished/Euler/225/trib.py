cache = {1:1,2:1,3:1}
def tribonacci(n):
    if n in cache: return cache[n]
    t = tribonacci
    ret = t(n-1) + t(n-2) + t(n-3)
    cache[n] = ret
    return ret

modCaches = [{1:1,2:1,3:1} for _ in range(10**5)]
def tribonacciMod(n, mod):
    if n in modCaches[mod]: return modCaches[mod][n]
    t = lambda x: tribonacciMod(x, mod)
    ret = (t(n-1) + t(n-2) + t(n-3)) % mod
    modCaches[mod][n] = ret
    return ret

def findPattern(ls):
    for i in range(len(ls)-4):
        for j in range(i+1, len(ls)):
            if ls[i:i+4] == ls[j:j+4]:
                print(i, j)
                return True
    return False

count = 0
for x in range(25, 10**5, 2):
    #tribs = [tribonacci(n) % x for n in range(1,x*24)]
    #print(x)
    tribs = [tribonacciMod(n, x) for n in range(1, x*24)]
    if 0 not in tribs:
        count += 1
        if count == 124:
            print(x)
            break
