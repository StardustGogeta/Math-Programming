def rMax2(a):
    if a % 2:
        return a**2 - a
    return a**2 - 2*a

print(sum(rMax2(a) for a in range(3, 1001)))
