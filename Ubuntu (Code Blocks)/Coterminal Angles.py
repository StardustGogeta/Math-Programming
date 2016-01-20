def coterminal(orig):
    ang1, ang2 = orig, orig
    if orig > 0:
        if orig > 360:
            while ang1 > 360:
                ang1 -= 360
            ang2 = ang1 - 360
        else:
            ang1 += 360
            ang2 -= 360
    elif orig < -360:
        while ang1 < -360:
            ang1 += 360
        ang2 = ang1 + 360
    else:
        ang1 -= 360
        ang2 += 360
    return("The coterminal angles include "+str(ang1)+" and "+str(ang2)+".")

#coterminal(int(input("Please state an angle.\n")))
