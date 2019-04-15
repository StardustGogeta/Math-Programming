pDCount = 9
pDSides = 4
cDCount = 6
cDSides = 6

pSums = dict()
for x in range(1,37): pSums[x] = 0
for p in range(pDSides**pDCount):
    pDice = [(p // (pDSides**i) % pDSides) for i in range(pDCount)]
    pSums[sum(pDice)+pDCount] += 1
for s in pSums: pSums[s] /= pDSides**pDCount

cSums = dict()
for x in range(1,37): cSums[x] = 0
for c in range(cDSides**cDCount):
        cDice = [(c // (cDSides**i) % cDSides) for i in range(cDCount)]
        cSums[sum(cDice)+cDCount] += 1
# Results very similar to https://en.wikipedia.org/wiki/Centered_pentachoric_number
for s in cSums: cSums[s] /= cDSides**cDCount

chance = 0
for i in range(2, 37):
    for j in range(1, i):
        chance += pSums[i] * cSums[j]
print(chance)
