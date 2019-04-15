def isTriangle(n):
    return (-1+(1+8*n)**.5)/2 % 1 == 0

data = open("p042_words.txt")
words = [s[1:-1] for s in data.read().split(",")]
data.close()
print(sum(isTriangle(sum(ord(c)-64 for c in s)) for s in words))
