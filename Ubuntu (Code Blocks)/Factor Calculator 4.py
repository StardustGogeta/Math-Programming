import math

def calculate(n):
    if n > 0:
        for d in range(1, int(math.sqrt(n))+1):
            if (n % d == 0):
                print(int(n/d), "\n", d)
        print("The list of factors has been successfully generated.\n")
    else:
        print("Are you trying to kill me?\nYou will pay for that.\n")
    return 0

calculate(int(input("What is the number?\n")))
