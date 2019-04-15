
def roman(n):
    ret = ''
    while n > 999:
        n -= 1000
        ret += 'M'
    if n > 899:
        n -= 900
        ret += 'CM'
    elif n > 399:
        if n < 500:
            n -= 400
            ret += 'CD'
        else:
            n -= 500
            ret += 'D'
    # n is guaranteed to be < 400
    ret += 'C' * (n // 100)
    n %= 100
    # n is guaranteed to be < 100
    if n > 89:
        n -= 90
        ret += 'XC'
    elif n > 39:
        if n < 50:
            n -= 40
            ret += 'XL'
        else:
            n -= 50
            ret += 'L'
    # n is guaranteed to be < 40
    ret += 'X' * (n // 10)
    n %= 10
    # n is guaranteed to be < 10
    if n > 8:
        n -= 9
        ret += 'IX'
    elif n > 3:
        if n < 5:
            n -= 4
            ret += 'IV'
        else:
            n -= 5
            ret += 'V'
    # n is guaranteed to be < 4
    ret += 'I' * n
    return ret

def fromRoman(s):
    ret = 0
    s += '#'
    try:
        while s[0] == 'M':
            s = s[1:]
            ret += 1000
        while s[0] == 'D':
            s = s[1:]
            ret += 500
        while s[0] == 'C':
            if s[1] == 'M':
                s = s[2:]
                ret += 900
            elif s[1] == 'D':
                s = s[2:]
                ret += 400
            else:
                s = s[1:]
                ret += 100
        while s[0] == 'L':
            s = s[1:]
            ret += 50
        while s[0] == 'X':
            if s[1] == 'C':
                s = s[2:]
                ret += 90
            elif s[1] == 'L':
                s = s[2:]
                ret += 40
            else:
                s = s[1:]
                ret += 10
        while s[0] == 'V':
            s = s[1:]
            ret += 5
        while s[0] == 'I':
            if s[1] == 'X':
                s = s[2:]
                ret += 9
            elif s[1] == 'V':
                s = s[2:]
                ret += 4
            else:
                s = s[1:]
                ret += 1
    except IndexError: pass
    return ret

# Test Code: all(fromRoman(roman(x))==x for x in range(1, 100000))
data = open('p089_roman.txt')
nums = data.read().splitlines()
data.close()
savings = 0
for num in nums:
    savings += len(num) - len(roman(fromRoman(num)))
print(savings)




        
