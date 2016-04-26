fib = [0,1]
print(fib[-1])
print(fib[-2])
for x in range(1,int(input('fib '))):
    fib.extend([int(fib[-1]+fib[-2])])
print(fib[-1])
input()
