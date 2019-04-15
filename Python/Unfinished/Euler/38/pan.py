
def pandigitalStr(s):
    return ''.join(sorted(s)) == "123456789"

h = 10**8
for x in range(1, 10**4):
    s = ''
    f = 1
    while len(s) < 9:
        s += str(x*f)
        f += 1
    if pandigitalStr(s):
        h = max(h, int(s))
        print(x)
print(h)
