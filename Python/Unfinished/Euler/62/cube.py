cubes = dict()
n = 5
mini = 10**100
for x in range(1,30000):
    x3 = x**3
    s = ''.join(sorted(str(x3)))
    if s in ['012334556789',
'012334566789',
'1123455566789',
'0012344556789',
'0234556677899',
'01122345677889',
'01223445567889']:
        #print(x3)
        mini = min(mini, x3)
    if s in cubes:
        cubes[s] += 1
    else:
        cubes[s] = 1
    #print(x, x3)
##    perms = set(int(''.join(s)) for s in itertools.permutations(str(x3)) if s[0]!='0')
##    #if x==773:
##    #    print(sum(map(isCube, perms)))
##    #    print(sum(map(isCube, perms)))
##     #   print(list(filter(isCube, perms)))
##    if sum(map(isCube, perms)) == n:
##        print(x3)
##        break
print(mini)

##for x in cubes:
##    if cubes[x] == n:
##        #perms = set(int(''.join(s)) for s in itertools.permutations(str(x)) if s[0]!='0')
##        #print(sum(map(isCube, perms)))
##        #print(list(filter(isCube, perms)))
##        print(x)
