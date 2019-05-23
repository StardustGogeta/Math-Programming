ret = ""

def move(n, F, T, U):
    if n == 1:
        global ret
        ret += ("Move top from " + str(F) + " to " + str(T)) + "\n"
    else:
        move(n-1, F, U, T)
        move(1, F, T, U)
        move(n-1, U, T, F)

move(3, "L", "R", "C")
print(ret)

# Output of function has 2**n-1 lines/movements
# Alternatively, you could say that it increases output by 2**n lines
