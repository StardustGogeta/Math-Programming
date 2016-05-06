import string, math

def fit(attempt):
    fitness = 0
    try:
        for e in x:
            e = int(e)
            if int(y[x.index(str(e))]) == eval(attempt):
                fitness += 1
        #print(attempt+" is legal")
        return fitness
    except:
        return 0


x = input("What is the input number set, separated with spaces?\n").split(' ')
y = input("What is the output number set, separated with spaces?\n").split(' ')
z = input("Extra options? (See source for full list.)\n").split(' ')
# Options:
# 1. Minimum complexity (default is 1)
# 2. Charset used (0: basic, 1: advanced)
# 3. Maximum complexity (default is 6)
z[0] = 1 if z[0]=='' else z[0]
charsets = ["e0123456789%+-*/z","""e\\0123456789%+-_=/*^,;!()'{}[]:\"z"""]
chars = charsets[int(z[1])] if len(z)>1 else charsets[0]
max = int(z[2]) if len(z)>2 else 6
fitness, bestFit, indices, attempt = 0,0,[0],''
for _ in range(1,int(z[0])):
    indices.extend([0])
while fitness < len(x):
    for a in indices:
        attempt += chars[a]
    fitness = fit(attempt)
    if bestFit < fitness:
        bestFit = fitness
        print("    {0} received a fitness of {1}.".format(attempt,fitness))
    indices[-1] += 1
    addLen = 1
    for a in indices:
        if a+1 < len(chars):
            addLen = 0
            break
    if addLen:
        if max>1:
            indices.extend([0])
            for a in range(len(indices)):
                indices[a] = 0
            max -= 1
            print("\nExtending the attempt to {0} characters.\n".format(len(indices)))
        else:
            print("\nThe maximum attempt length has been reached.")
            break
    for b in range(len(indices)):
        for a in range(len(indices)):
            if indices[a] == len(chars):
                indices[a-1] += 1
                indices[a] = 0
    attempt = attempt[:-len(indices)]
    
