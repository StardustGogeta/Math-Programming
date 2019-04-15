data = open('p079_keylog.txt')
nums = set(int(x) for x in data.read().splitlines())
data.close()

password = '73162890'
def fitPassword(n):
    for x in range(len(password)-2):
        for y in range(x+1, len(password)-1):
            for z in range(y+1, len(password)):
                if int(password[x]+password[y]+password[z]) == n: return True
    return False

allChars = set()
for n in nums:
    allChars = allChars.union(set(str(n)))
print(nums)

for x in nums:
    print(x, fitPassword(x))
