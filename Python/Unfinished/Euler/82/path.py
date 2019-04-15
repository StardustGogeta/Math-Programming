import copy
data = open('p082_matrix.txt')
board = [[int(x) for x in row.split(',')] for row in data.read().splitlines()]
#board = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
original = copy.deepcopy(board)
data.close()

x = len(board) - 2
while x > -1:
    for row in board:
        row[x] += row[x + 1]
    changeFlag = True
    while changeFlag:
        #print([row[x] for row in board])
        changeFlag = False
        for y in range(len(board)):
            if 0 < y < len(board)-1 and (board[y-1][x] < board[y][x+1] or board[y+1][x] < board[y][x+1]):
                m = min(board[y-1][x], board[y+1][x])
                if board[y][x] != original[y][x] + m:
                    board[y][x] = original[y][x] + m
                    changeFlag = True
                    #print(y)
            else:
                if y > 0 and board[y-1][x] < board[y][x+1]:
                    if board[y][x] != original[y][x] + board[y-1][x]:
                        board[y][x] = original[y][x] + board[y-1][x]
                        changeFlag = True
                        #print(y)
                if y < len(board)-1 and board[y+1][x] < board[y][x+1]:
                    if board[y][x] != original[y][x] + board[y+1][x]:
                        board[y][x] = original[y][x] + board[y+1][x]
                        changeFlag = True
                        #print(y,'2')
    x -= 1
print(min(row[0] for row in board))
            
