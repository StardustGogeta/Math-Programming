import numpy

numpy.polyfit([1, 2, 3, 4],[1, 8, 27, 64], 1)

DEG = 10

def u(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
    #return n**3

def OP(k, n):
    xs = list(range(1, k+1))
    ys = list(map(u, xs))
    coeffs = numpy.polyfit(xs, ys, k-1)
    print(xs, ys, coeffs)
    return round(sum(coeffs[x]*n**(k-x-1) for x in range(len(coeffs))))

#for k in range(1, DEG+1):
print(sum(OP(k, k+1) for k in range(1, DEG+1)))
