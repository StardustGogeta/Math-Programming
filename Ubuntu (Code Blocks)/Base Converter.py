from math import *

def convert(fN,fB,sB):
    try:
        tVT=int(str(fN),fB)
        sN=""
        while tVT:
            sN+=str(tVT%sB)
            tVT//=sB
        return(sN[::-1])
    except ValueError:
        return("Error 003: Invalid input detected/")

#convert(int(input("What is the number?\n")),
#          int(input("What is the current base? (1 < x < 11)\n")),
#          int(input("What is the desired base? (1 < x < 11)\n")))
#11110100001000111111 is 999999 in base 10
