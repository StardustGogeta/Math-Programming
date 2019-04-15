
##def reasonable(s):
##    return 'the' in s
##    return True
##    blacklist = ['=', '$', '}', '+', '4']
##    for c in blacklist:
##        if c in s:
##            return False
##    return True

# himself, beginning
data = open('p059_cipher.txt')
code = [int(x) for x in data.read().split(',')]
data.close()
##for A in range(97, 123):
##    for B in range(97, 123):
##        for C in range(97, 123):
##            newCode = list(code)
##            key = [A, B, C]
##            for i in range(len(newCode)):
##                newCode[i] ^= key[i % 3]
##            msg = ''.join(chr(x) for x in newCode)
##            if reasonable(msg):
##                print(msg,A,B,C)
A = 103
B = 111
C = 100
newCode = list(code)
key = [A, B, C]
for i in range(len(newCode)):
    newCode[i] ^= key[i % 3]
msg = ''.join(chr(x) for x in newCode)
print(msg)
print(sum(newCode))
