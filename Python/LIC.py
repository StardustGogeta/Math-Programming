def calcslope(A,B,C,D,E,F,G,H):
    try:
        s=(D-B)/(C-A)
        s2=(H-F)/(G-E)
        y1=B-(s*A)
        y2=F-(s2*E)
        x=(y2-y1)/(s-s2)
        y3=s*x+y1
        return("The point of intersection is ("+str(round(x,3))+", "+str(round(y3,3))+").")
    except(ZeroDivisionError):
        return("Error 001: Vertical or parallel lines detected.")

def convert(s,s2,y1,y2):
    try:
        x=(y2-y1)/(s-s2)
        y3=s*x+y1
        return("The point of intersection is ("+str(round(x,3))+", "+str(round(y3,3))+").")
    except(ZeroDivisionError):
        return("Error 002: Vertical or parallel lines detected.")

    
#convert(int(input("Enter coordinate pairs for two lines (0) or equations (1).\n")))
