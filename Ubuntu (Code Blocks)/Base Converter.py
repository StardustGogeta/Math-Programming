from math import *

def convert(fN,fB,sB):
    if int(fB)>10 or int(fB)<2 or int(sB)>10 or int(sB)<2:
        return("Stop wasting time.")
    else:
        tVT=0
        while fN>0:
            C=fN
            d=int(floor(log10(C)))
            C/=10**d
            dP=10**d
            dV=fB**d
            tV=int(C)*dV
            fN-=int(C)*dP
            tVT+=tV
        sN=0
        tVTN=1
        while tVTN>0:
            Z=int(floor(log10(tVT)/log10(sB)))
            dV=sB**Z
            tVTN=int(tVT)%dV
            sN+=(tVT-tVTN)*10**Z/dV
            tVT=tVTN
        return(int(sN))

#convert(int(input("What is the number?\n")),
#          int(input("What is the current base? (1 < x < 11)\n")),
#          int(input("What is the desired base? (1 < x < 11)\n")))
