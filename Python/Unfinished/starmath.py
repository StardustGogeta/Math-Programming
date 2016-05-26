import copy

class math:
    # 4X slower than math.ceil(x)
    def ceil(x):
        return int(x//1+1)

    # 4X slower than math.floor(x)
    def floor(x):
        return int(x//1)
    
    # Incredibly slower than math.log10(x)
    def log(x): # 0.586 sec
        n,y = 0,1
        x,z = x,1 if x > 1 else 1/x,-1
        for a in range(16):
            while x>10.**(n+y):
                n += y
            y /= 10
        return n*z
            
    # Significantly faster than math.copysign(x,1)
    def sgn(x):
        return 1 if x>=0 else -1

class matrix:
 
    # Display matrices nicely.
    def disp(a): # Displays the matrix as a 2D array.
        return str(a)[1:-1].replace('], ',']\n')
    def flat(a): # Flattens the matrix into a single list.
        return [A for b in a for A in b]
    
    # Creating new matrices.
    def zero(x,y): # Creates a matrix of only zeros with given dimensions.
        return [[0 for b in range(y)] for a in range(x)]
    def ident(x): # Creates a square identity matrix of the given order.
        A = matrix.zero(x,x)
        for a in range(x):
            A[a][a] = 1
        return A
    def new(x,y): # Creates a matrix of the given dimensions with values corresponding to position.
        return [[b for b in range(y)] for a in range(x)]
    def fill(x,y,z): # Creates a matrix with given dimensions, filled with one number.
        return [[z for b in range(y)] for a in range(x)]
    
    # Manipulating existing matrices.
    def add(a,b): # Adds two matrices of the same dimensions.
        assert (len(a),len(a[0]))==(len(b),len(b[0])), "The matrices are not of the same dimensions."
        return [[a[x][y]+b[x][y] for y in range(len(a))] for x in range(len(a[0]))]
    def sub(a,b): # Subtracts two matrices of the same dimensions.
        assert (len(a),len(a[0]))==(len(b),len(b[0])), "The matrices are not of the same dimensions."
        return [[a[x][y]-b[x][y] for y in range(len(a))] for x in range(len(a[0]))]
    def scale(a,s): # Scales every element of a matrix by a factor.
        return [[a[x][y]*s for y in range(len(a))] for x in range(len(a[0]))]
    def mult(a,b): # Multiplies two matrices of the correct dimensions.
        assert len(a[0])==len(b), "The matrices are not of the correct dimensions."
        return [[sum([e*f for e,f in zip(a[x],[b[A][y] for A in range(len(b))])]) for y in range(len(b[0]))] for x in range(len(a))]
    def trans(a): # Transposes a given matrix.
##        c = matrix.new(len(a),len(a[0]))
##        for x in range(len(a)):
##            for y in range(len(a[0])):
##                c[x][y]=a[y][x]
##        return c
        return [[a[y][x] for y in range(len(a))] for x in range(len(a[0]))]
    def coftr(a): # Creates the matrix of cofactors.
        return [[a[x][y]*(-1)**(x+y) for y in range(len(a))] for x in range(len(a[0]))]
    def adj(a): # Creates the adjoint matrix of the input.
        return [[a[y][x]*(-1)**(x+y) for y in range(len(a))] for x in range(len(a[0]))]
    def det(a): # Finds the determinant of a square matrix.
        if len(a)==2:
            return a[0][0]*a[1][1]-a[0][1]*a[1][0]
        else:
            c = 0
            for y in range(len(a[0])):
                b = copy.deepcopy(a)
                b.pop(0)
                for X in b:
                    X.pop(y)
                c += a[0][y]*matrix.det(b)*((y%2)*-2+1)
            return c
    def minors(a): # Calculates the matrix of minors.
        c = matrix.new(len(a),len(a[0]))
        for x in range(len(a)):
            for y in range(len(a[0])):
                b = copy.deepcopy(a)
                b.pop(x)
                for X in b:
                    X.pop(y)
                c[x][y]=matrix.det(b)
        return c
    def inv(a): # Calculates the inverse of a given matrix.
        return matrix.scale(matrix.adj(matrix.minors(a)),1/matrix.det(a))

# Test cases for the more advanced matrix functions.
#import time, math
#A = [[4,5,1],[2,3,1],[0,8,90]]
#B = [[3,0,2],[2,0,-2],[0,1,1]]
#C = [[2,3],[1,2]]
#D = [[2,0,-2],[0,6,-3],[0,2,0]]
#E = [[1,2,-2],[4,0,-3],[5,0,0]]
#F = [[3,0,2,-1],[1,2,0,-2],[4,0,6,-3],[5,0,2,0]]
#G = [[1,0,1,0,1],[2,3,4,1,7],[2,1,4,6,1],[0,1,5,3,1],[2,4,2,4,2]]
#1 0 1 0 1 2 3 4 1 7 2 1 4 6 1 0 1 5 3 1 2 4 2 4 2
#print(str(matrix.det(C))+'\n')
#print(str(matrix.det(D))+'\n')
#print(str(matrix.det(E))+'\n')
#print(str(matrix.det(F))+'\n')
#print(matrix.disp(matrix.inv(G))+'\n')

# CES Comparison with numpy
#import numpy as np
#a,b,c,d,e,f = -2,7,-9,0,-10,-5
#start = time.clock()
#for x in range(300):
#    DEF = matrix.mult(matrix.inv([[a,b,1],[c,d,1],[e,f,1]]),[[-(a**2+b**2)],[-(c**2+d**2)],[-(e**2+f**2)]])
#    D,E,F = DEF[0][0]/2,DEF[1][0]/2,DEF[2][0]
#print(time.clock()-start,"seconds for stardust")
#print("(x - {0})² + (y - {1})² = {2}".format(round(-D,3),round(-E,3),round(-F+D**2+E**2,3)))
#mat = np.matrix
#start = time.clock()
#for x in range(300):
#    DEF = mat([[a,b,1],[c,d,1],[e,f,1]]).I * mat([[-(a**2+b**2)],[-(c**2+d**2)],[-(e**2+f**2)]])
#    D,E,F = DEF[0].A1[0]/2,DEF[1].A1[0]/2,DEF[2].A1[0]
#print(time.clock()-start,"seconds for numpy")
#print("(x - {0})² + (y - {1})² = {2}".format(round(-D,3),round(-E,3),round(-F+D**2+E**2,3)))


