import time
from random import random
def cf(h,f,t):
    start = time.clock()
    s = 0
    for x in range(t):
        r = 0
        for x in (random() for x in range(f)):
            r += 1 if x>=.5 else 0
        s += 1 if r==h else 0
    print("This combination will happen {0}% of the time.".format(s/t*100))
    print(time.clock()-start,"seconds")

cf(int(input("How many heads?\n")),int(input("How many flips?\n")),int(input("How many tests?\n")))

import subprocess
a = '34'
filepath="C:/Users/Gerst/Documents/GitHub/Math-Programming/Python/ProbabilitySim/rand.exe "+a
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
p = subprocess.Popen(filepath, startupinfo=startupinfo, stdout = subprocess.PIPE)
stdout, stderr = p.communicate()
print(p.returncode)

