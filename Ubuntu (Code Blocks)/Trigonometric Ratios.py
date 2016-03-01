from math import *

def trig(ang,o,rad):
    pi=atan(1)*4
    if ang==1:
        o=o*pi/180
    else:
        if rad==3:
            o=pi*o;
    return("sin = "+str(round(sin(o),3)),"cos = "+str(round(cos(o),3)),"tan = "+str(round(tan(o),3)),"csc = "+str(round(1/sin(o),3)),"sec = "+str(round(1/cos(o),3)),"cot = "+str(round(1/tan(o),3)))

#trigratios(int(input("Degrees (0) or radians (1)?\n")),float(input("What is the angle measure?\n")))
