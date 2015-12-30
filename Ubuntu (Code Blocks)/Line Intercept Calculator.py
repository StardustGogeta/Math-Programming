def calcslope(A,B,C,D,E,F,G,H):
    global s,s2,y1,y2
    s = (D-B)/(C-A)
    s2 = (H-F)/(G-E)
    y1 = B-(s*A)
    y2 = F-(s2*E)

def calculate(r):
    global s,s2,y1,y2
    if (r == 0):
        calcslope(float(input("\nLine 1\n_________________________\nCoordinate Pair 1\nX: ")),
            float(input("Y: ")),
            float(input("Coordinate Pair 2\nX: ")),
            float(input("Y: ")),
            float(input("\nLine 2\n_________________________\nCoordinate Pair 1\nX: ")),
            float(input("Y: ")),
            float(input("Coordinate Pair 2\nX: ")),
            float(input("Y: ")))
    else:
        s,y1,s2,y2 = float(input("\nSlope 1: ")),float(input("Y-Intercept 1: ")),float(input("Slope 2: ")),float(input("Y-Intercept 2: "))
    x=(y2-y1)/(s-s2)
    y3=(s-s2)*x+y2
    print("\nThe point of intersection is (",x,",",y3,").")

calculate(int(input("Enter coordinate pairs for two lines (0) or equations (1).\n")))
