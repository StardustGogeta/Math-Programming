from numpy import matrix

# Given three coordinate points, this will find the equation of the circle
# which passes through them.
a,b,c,d,e,f = input('List the three coordinate points, separated by commas.\n').split(',')
for x in 'abcdef':
    exec('{0}=int({0})'.format(x))
#a,b,c,d,e,f = -2,7,-9,0,-10,-5
mat1 = matrix([[-(a**2+b**2)],
              [-(c**2+d**2)],
              [-(e**2+f**2)]])
mat2 = matrix([[a,b,1],
               [c,d,1],
               [e,f,1]]).I
DEF = mat2 * mat1
D,E,F = DEF[0].A1[0]/2,DEF[1].A1[0]/2,DEF[2].A1[0]
print("(x - {0})² + (y - {1})² = {2}".format(round(-D,3),round(-E,3),round(-F+D**2+E**2,3)))
