
def repLength(n):
    rems = []
    extra = 0
    num = 10
    while num not in rems:
        rems += [num]
        while num < n:
            num *= 10
            extra += 1
        num %= n
        num *= 10
        if not num: return 0
    #print(rems, extra)
    return len(rems)+extra

def indOfMax(ls):
    return ls.index(max(ls))

print(indOfMax([repLength(x) for x in range(1,1000)])+1)


        
