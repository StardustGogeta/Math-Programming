import math, itertools

def prime(n):
    for d in range(2, math.floor(math.sqrt(n))+1):
        if not n % d: return False
    return True

for x in range(1001, 10**4, 2):
    xs = list(set(filter(prime, (int(''.join(n)) for n in itertools.permutations(str(x))))))
    xs.sort()
    if len(xs) >= 3 and x == min(xs):
        for y in range(len(xs)-2):
            for z in range(y+1, len(xs)-1):
                if 2*xs[z]-xs[y] in xs:
                    print(xs[y], xs[z], 2*xs[z]-xs[y])
