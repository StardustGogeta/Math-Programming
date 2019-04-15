import itertools

summation = 0
for num in  itertools.permutations("0123456789"):
    if num[0] == '0': continue
    num = ''.join(num)
    if not int(num[7:]) % 17:
        if not int(num[6:9]) % 13:
            if not int(num[5:8]) % 11:
                if not int(num[4:7]) % 7:
                    if not int(num[3:6]) % 5:
                        if not int(num[2:5]) % 3:
                            if not int(num[1:4]) % 2:
                                summation += int(num)
print(summation)
