import math, operator

def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def is_prime(x):
    return all(x%d for d in range(2, 1+math.floor(math.sqrt(x))))

def get_prime_factor(x):
    for d in range(2, 1+math.floor(math.sqrt(x))):
        if not x % d: return d
    return x

# __________________________

def pe18():
    triangle = """75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")
    triangle = [[int(n) for n in row.split()] for row in triangle]
    #print(triangle)
    for y in range(len(triangle)-2,0,-1):
        for x in range(y+1):
            triangle[y][x] += max(triangle[y+1][x], triangle[y+1][x+1])
    print(triangle[0][0]+max(triangle[1]))

def pe33():
    for x in range(10,100):
        for y in range(x+1,100):
            a, b = str(x), str(y)
            if a[0] in b:
                if a[0] == b[0]:
                    if int(a[1])/int(b[1]) == x/y:
                        print(x,y)
                else:
                    if int(a[1])/int(b[0]) == x/y:
                        print(x,y)
            elif a[1] in b and a[1] != '0':
                if a[1] == b[0] and b[1] != '0':
                    if int(a[0])/int(b[1]) == x/y:
                        print(x,y)
                else:
                    if int(a[0])/int(b[0]) == x/y:
                        print(x,y)
                

def pe35():
    derp = 0
    for x in range(2,10**6):
        X = str(x)*2
        L = len(X)//2
        bad = False
        for n in range(L):
            num = int(X[n:n+L])
            if not is_prime(num):
                bad = True
        if not bad:
            derp += 1
    return derp

def pe47():
    def distinct_primes_count(n):
        f = set()
        while n > 1:
            prime = get_prime_factor(n)
            n /= prime
            f.add(prime)
        return len(f)
    counts = list(map(distinct_primes_count, range(2*3*5*7, 1000000)))
    print(counts[:100])
    for x in range(len(counts)):
        if counts[x] == 4 and counts[x] == counts[x+1] and counts[x] == counts[x+2] and counts[x] == counts[x+3]:
            print(x+2*3*5*7)

def pe67():
    tri = open("p067_triangle.txt")
    triangle = tri.read().splitlines()
    tri.close()
    triangle = [[int(n) for n in row.split()] for row in triangle]
    #print(triangle)
    for y in range(len(triangle)-2,0,-1):
        for x in range(y+1):
            triangle[y][x] += max(triangle[y+1][x], triangle[y+1][x+1])
    print(triangle[0][0]+max(triangle[1]))

def pe81():
    mat = open("p081_matrix.txt")
    matrix = mat.read().splitlines()
    mat.close()
    matrix = [[int(n) for n in row.split(',')] for row in matrix]
    #matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
    L = len(matrix)-1
    #print(matrix)
    #print(matrix[0][0])
    for rowColumnSum in range(L*2-1,L-1,-1):
        for y in range(L,rowColumnSum-L-1,-1):
            x = rowColumnSum-y
            #print(str(y)+" "+str(x)+" "+str(rowColumnSum))
            if y == L: matrix[y][x] += matrix[y][x+1]
            elif x == L: matrix[y][x] += matrix[y+1][x]
            else:
                #print(matrix[y+1][x], matrix[y][x+1])
                matrix[y][x] += min(matrix[y+1][x], matrix[y][x+1])
    for rowColumnSum in range(L-1,-1,-1):
        for y in range(rowColumnSum,-1,-1):
            x = rowColumnSum-y
            #print(y, x, rowColumnSum)
            matrix[y][x] += min(matrix[y+1][x], matrix[y][x+1])
    print(matrix[0][0], '\n'.join(str(r[:10]) for r in matrix[:10]))

##def pe493():
##    f = math.factorial
##    E = 0
##    E += 0 * (f(50)/f(30)) / (f(70)/f(50)) * choose(70,0)
##    E += 1 * 
##    pass

def pe587():
    A = 0
    res = 10000000
    slope = 1/2239
    for rect in range(res):
        x = rect/res
        y = min(slope*x,1-math.sqrt(2*x-x**2))
        #print(slope*x,1-(2*x-x**2)**.5)
        A += y
    return A/(1-math.pi/4)/res
