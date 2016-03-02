import math

def convert(n):
    if n > 0:
        numbers=[]
        for d in range(1, int(math.sqrt(n))+1):
            if (n % d == 0):
                numbers.append(int(n/d))
                numbers.append(d)
        return(numbers)
    else:
        return("Error!")

#convert(int(input("What is the number?\n")))
