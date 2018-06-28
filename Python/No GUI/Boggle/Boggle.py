from time import perf_counter as clock
start = clock()
txt = open("english_words.txt")
english = sorted(x for x in txt.read().upper().splitlines() if 2 < len(x) < 18)
txt.close()

def findConsecutiveEligible(s, d, words = english):
    elig = 0
    for word in words:
        try:
            if word[d] == s:
                elig = 1
                yield word
            elif elig:
                break
        except IndexError: pass

def getAdjacentCoords(coords): # path consists of letters already used
    y, x = coords
    adj = []
    if x > 0: adj.append((y, x-1))
    if x < 3: adj.append((y, x+1))
    if y > 0:
        adj.append((y-1, x))
        if x > 0: adj.append((y-1, x-1))
        if x < 3: adj.append((y-1, x+1))
    if y < 3:
        adj.append((y+1, x))
        if x > 0: adj.append((y+1, x-1))
        if x < 3: adj.append((y+1, x+1))
    return adj

b = open("board.txt")
boardTxt = b.read()
b.close()
board = [boardTxt[x*4:(x+1)*4] for x in range(4)] # Would have to be rewritten for Qu combo
#print(board)

def formWords(coords, board, path, master, depth = 0, tempWord = '', prevSubset = english):
    char = board[coords[0]][coords[1]]
    tempWord += char
    wordsSubset = list(findConsecutiveEligible(char, depth, prevSubset))
    if len(wordsSubset):
        path.append(coords)
        if depth > 1 and tempWord in prevSubset:
            master.add(tempWord)
        for c in getAdjacentCoords(coords):
            if c not in path:
                formWords(c, board, list(path), master, depth + 1, tempWord, wordsSubset)

masterList = set()
for y in range(4):
    for x in range(4):
        formWords((y, x), board, list(), masterList)

masterList = sorted(masterList)
print(str(len(masterList))+' '.join(masterList))
out = open('out.txt', 'w')
out.write(' '.join(masterList))
out.close()
print(clock()-start)
