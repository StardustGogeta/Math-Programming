import math, itertools

balls = [0, 1, 2, 3, 4, 5, 6] * 10
#print(balls)
totalExpected = 0
for comb in itertools.combinations(balls, 20):
    totalExpected += len(set(comb))
print(totalExpected/(math.factorial(70)//math.factorial(20)//math.factorial(50)))

