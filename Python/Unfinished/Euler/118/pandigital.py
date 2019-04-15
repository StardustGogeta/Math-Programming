import math, itertools

def prime(n):
    if n == 1: return False
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True

def fixSetFormat(p):
    #print(p)
    ret = set()
    acc = ''
    for c in p:
        if c == ',':
            ret.add(int(acc))
            acc = ''
        else:
            acc += c
    ret.add(int(acc))
    return ret

successes = []
chars = '123456789'
perms = list(list(p) for p in itertools.permutations(chars))
for p in perms:
    for commaIndex in range(2**8):
        commaAdjustedP = list(p)
        for i in range(7, -1, -1):
            if commaIndex & 2**i:
                commaAdjustedP.insert(i+1, ',')
        finalSet = fixSetFormat(commaAdjustedP)
        if finalSet not in successes:
            if all(prime(n) for n in finalSet):
                successes.append(finalSet)
print(len(successes))
