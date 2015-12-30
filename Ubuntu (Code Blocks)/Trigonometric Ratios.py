from math import *

def trigratios(ang,o):
    pi=atan(1)*4
    if ang==0:
        o=o*pi/180
    else:
        rad=int(input("Is it in terms of pi? (Y=1)\n"))
        if rad==1:
            o=pi*o;
    print("sin = ",sin(o),"\ncos = ",cos(o),"\ntan = ",tan(o),"\ncsc = ",1/sin(o),"\nsec = ",1/cos(o),"\ncot = ",1/tan(o),"\n")

trigratios(int(input("Degrees (0) or radians (1)?\n")),float(input("What is the angle measure?\n")))
