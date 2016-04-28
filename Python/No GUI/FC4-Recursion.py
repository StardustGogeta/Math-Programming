import math

def fc4(x):
    check(x,math.sqrt(x))

def check(a,b):
    print('test')
    if a%b==0:
        print(b,a/b)
    if b>1:
        check(a,b-1)
    else:
        print("Done.")
