import math
def coterminal(o):
    o=o%360
    return("The coterminal angles include {0} and {1}.".format(o,o-math.copysign(360,o)))

#coterminal(int(input("Please state an angle.\n")))
