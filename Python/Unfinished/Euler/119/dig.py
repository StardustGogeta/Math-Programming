import math
count = 0
M = 15
n = 10
while count < M:
    n += 1
    try:
        digSum = 0
        n2 = n
        while n2:
            digSum += n2 % 10
            n2 //= 10
        exp = int(math.log(n, digSum))
        if digSum ** exp == n:
        #exp = math.log(n, digSum)
        #if abs(exp-int(exp)) < .00001:
            count += 1
            print(n, digSum, exp, count)
    except:
        # print(n)
        pass # Digit sum is 1
print(n)
