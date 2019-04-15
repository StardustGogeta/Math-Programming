def palindrome(n):
    s = str(n)
    return s == s[::-1]

def lychrel(n):
    for x in range(50):
        s = str(n)
        n += int(s[::-1])
        if palindrome(n): return False
    return True

print(sum(lychrel(x) for x in range(10000)))
