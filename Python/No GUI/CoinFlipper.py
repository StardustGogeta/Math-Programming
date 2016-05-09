from random import random
times = int(input("How many tests?\n"))
flips = int(input("How many heads?\n"))
flips2 = int(input("How many flips?\n"))
times2 = 0
for x in range(times):
    r = 0
    for x in (random() for x in range(flips2)):
        r += 1 if x >=.5 else 0
    times2 += 1 if r == flips else 0
print("This combination will happen {0}% of the time.".format(times2/times*100))
