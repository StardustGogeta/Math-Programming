from time import clock
start = clock()
txt = open("english_words.txt")
english = list(x for x in txt.read().upper().splitlines() if 2 < len(x) < 18)
txt.close()

def findWordsStartingWith(s, words = english):
    return list(x for x in words if x.startswith(s))

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

def formWords(coords, board, path, master, tempWord = '', prevSubset = english):
    tempWord += board[coords[0]][coords[1]]
    wordsSubset = findWordsStartingWith(tempWord, prevSubset)
    if len(wordsSubset):
        path.append(coords)
        if len(tempWord) > 2 and tempWord in prevSubset:
            master.add(tempWord)
        for c in getAdjacentCoords(coords):
            if c not in path:
                formWords(c, board, list(path), master, tempWord, wordsSubset)

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
