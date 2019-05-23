from numpy import matrix

# This uses matrix multiplication to find a polynomial
# of degree n from n+1 points on the curve.

points = [(-1,1),(0,0),(1,1)]
deg = len(points)-1

a = matrix([[x[1]] for x in points])
b = matrix([[x[0]**n for n in range(deg,-1,-1)] for x in points])

coeffs = b.I @ a
output = []
for x in range(deg,-1,-1):
    coeff = coeffs[deg-x,0]
    if coeff:
        output += [str(coeff)+'x^'+str(x)]
print(' + '.join(output))
