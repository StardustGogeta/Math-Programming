from time import clock
start = clock()
txt = open("english_words.txt")
english = list(filter(lambda x: len(x) < 18, txt.read().upper().splitlines()))
txt.close()

def findWordsStartingWith(s, words = english):
    ls = list(filter(lambda x: x.startswith(s), words))
    return ls

def getAdjacentCoords(coords, path): # path consists of letters already used
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
    return list(filter(lambda x: x not in path, adj))

b = open("board.txt")
boardTxt = b.read()
b.close()
board = [boardTxt[x*4:(x+1)*4] for x in range(4)] # Would have to be rewritten for Qu combo
#print(board)

def formWords(coords, board, path, tempWord = '', prevSubset = english):
    formed = []
    y, x = coords
    tempWord += board[y][x]
    path.append(coords)
    if len(tempWord) > 2 and tempWord in prevSubset:
        formed += [tempWord]
    wordsSubset = findWordsStartingWith(tempWord, prevSubset)
    if len(wordsSubset):
        for c in getAdjacentCoords(coords, path):
            formed += formWords(c, board, list(path), tempWord, wordsSubset)
    return formed

masterList = []
for y in range(4):
    for x in range(4):
        masterList += formWords((y, x), board, list()) # Removing list() causes path to break because of list wackiness
        print("Cell complete")

masterList = sorted(list(set(masterList)))
print(' '.join(masterList))
out = open('out.txt', 'w')
out.write(' '.join(masterList))
out.close()
print(clock()-start)
