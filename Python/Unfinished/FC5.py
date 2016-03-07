import math

def convert(n):
    numlist=[1]
    c=n
    while n-1:
        try:
            f = findFactor(n)
            n /= f
            y=len(numlist)
            for x in range(y):
                numlist.extend([f*numlist[x]])
                numlist=list(set(numlist))
                numlist.sort()
                print(f,n,numlist)
        except TypeError:
            y=len(numlist)-1
            for x in range(y):
                numlist.extend([int(n)*numlist[x]])
                numlist=list(set(numlist))
                numlist.sort()
            break
    numlist.extend([c])
    print("Finish", numlist)

def findFactor(n):
    for d in range(2, math.ceil(math.sqrt(n))):
        if (n % d == 0):
            return(int(d))
            break

convert(int(input("What is the number?\n")))
