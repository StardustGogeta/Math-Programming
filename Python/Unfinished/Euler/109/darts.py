from itertools import chain

scores = []
for zone in chain(range(1, 21), [25]):
    scores.append(("S"+str(zone), zone))
    scores.append(("D"+str(zone), zone*2))
    if zone != 25: scores.append(("T"+str(zone), zone*3))

# print(len(scores)) -> 62
checkouts = 0
target = 100
for end in scores:
    if end[0][0] == "D": # Double
        c = end[1]
        if c < 100: checkouts += 1
        for i in range(len(scores)):
            if scores[i][1] + c < 100:
                checkouts += 1
                for j in range(i, len(scores)):
                    if scores[i][1] + scores[j][1] + c < 100:
                        checkouts += 1
print(checkouts)
