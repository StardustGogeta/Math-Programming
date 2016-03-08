import math

def convert(n):
    if n > 0:
        numbers=[]
        for d in range(1, math.floor(math.sqrt(n)+1)):
            if (n % d == 0):
                numbers.extend([int(n/d),d])
        numbers.sort()
        return(numbers)
    else:
        return("Error!")

#convert(int(input("What is the number?\n")))
