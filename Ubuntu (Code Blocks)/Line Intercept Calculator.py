def calcslope(A,B,C,D,E,F,G,H):
    s=(D-B)/(C-A)
    s2=(H-F)/(G-E)
    y1=B-(s*A)
    y2=F-(s2*E)
    x=(y2-y1)/(s-s2)
    y3=s*x+y1
    return("The point of intersection is (",x,",",y3,").")

def convert(s,s2,y1,y2):
    x=(y2-y1)/(s-s2)
    y3=s*x+y1
    return("The point of intersection is (",x,",",y3,").")

#convert(int(input("Enter coordinate pairs for two lines (0) or equations (1).\n")))
