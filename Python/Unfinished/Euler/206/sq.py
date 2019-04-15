import math
def match(n):
    s = str(n)
    return s[0]=='1' and s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5' and s[10]=='6' and s[12]=='7' and s[14]=='8' and s[16]=='9' and s[18]=='0'

#print(math.sqrt(1020304050607080900), match(1020304050607080900))
magic = 10203040506070809
# Add a zero on the end of the printed result
for n in range(int(math.sqrt(magic)), int(math.sqrt(magic)*2)):
    if match(n**2*100):
        print(n)
        break
