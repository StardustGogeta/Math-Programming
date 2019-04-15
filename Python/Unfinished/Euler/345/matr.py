import itertools

matrix =  list(map(int, '''7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805'''.split()))

testCase = list(map(int, '''7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303'''.split()))

matrix = [matrix[15*i:15*(i+1)] for i in range(15)]
testCase = [testCase[5*i:5*(i+1)] for i in range(5)]
# print(matrix[1][1])

def remColumn(row, c):
    return [row[x] for x in range(len(row)) if x != c]

def newMatrix(mat, a, b):
    return [remColumn(mat[i], b) for i in range(len(mat)) if i != a]

def matSum(mat, lowerBound):
    if len(mat) == 1: return mat[0][0]
    #if len(mat) == 2:
        #return max(mat[0][1]+mat[1][0], mat[0][0]+mat[1][1])
##    M = (0, 0, 0)
##    for i in range(len(mat)):
##        for j in range(len(mat)):
##            n = mat[i][j]
##            if n > M[0]:
##                M = (n, i, j)
    #newMat = newMatrix(mat, M[1], M[2])
    #return M[0] + matSum(newMat)
    try: return max(mat[i][0] + matSum(newMatrix(mat, i, 0), lowerBound) for i in range(len(mat)) if mat[i][0] > lowerBound)
    except ValueError: raise ZeroDivisionError

def altMatSum(mat):
    selections = itertools.permutations(range(len(mat)))
    return max(sum(mat[i][select[i]] for i in range(len(mat))) for select in selections)
