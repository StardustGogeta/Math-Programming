coinValues = [1,2,5,10,20,50,100,200]
cache = dict()
def coinPartitions(n, prevVal = 0, flag = 0):
    if n == 0: return 0
    if not prevVal or prevVal > n:
        if n in cache:
            return cache[n]
        prevVal = n
    lowerCoins = [coin for coin in coinValues if coin <= prevVal]
    ret = sum(coinPartitions(n-nextVal, nextVal) for nextVal in lowerCoins)
    #if flag: print([(nextVal, coinPartitions(n-nextVal, nextVal)) for nextVal in lowerCoins])
    if n in coinValues and n <= prevVal: ret += 1
    if not prevVal or prevVal > n:
        cache[n] = ret
    return ret
