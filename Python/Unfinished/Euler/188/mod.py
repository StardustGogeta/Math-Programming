residues = {0:1}
residuesSet = set()
res = 1
# Using this method to check for duplicate residues, it was found that
# 1777^n is periodic mod 10^8 with period of 1250000
for n in range(1, 1250000): # Upper bound obtained via experimentation
    res = 1777*res % 10**8
    residuesSet.add(res)
    residues[n] = res

def getResidue(power):
    return residues[power % 1250000]

pwr = 1777
for x in range(1855):
    pwr = getResidue(pwr)
print(pwr)
