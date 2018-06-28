from copy import deepcopy

def dispBoard(board):
    for r in board:
        print(' '.join(['-','X','O'][c] for c in r))

def checkVictory(board,y,x,side):
    testBoard = deepcopy(board)
    testBoard[y][x] = side
    # Common row
    if testBoard[y] == [side]*3:
        return True
    # Common column
    if [r[x] for r in testBoard] == [side]*3:
        return True
    # Common diagonal
    if [testBoard[n][n] for n in range(3)] == [side]*3:
        return True
    if [testBoard[n][2-n] for n in range(3)] == [side]*3:
        return True
    else:
        return False

def getValidPlayerInput(board):
    y,x = 3,3
    while 1:
        try:
            y = int(input("Y: "))
            x = int(input("X: "))
        except:
            print('Invalid input.')
            continue
        if board[y][x]:
            print("Cell already taken.")
        elif not (y in range(3) and x in range(3)):
            print("Cell out of range.")
        else:
            return y,x

def getCPUInput(board,side):
    if not board[1][1]:
        return 1,1
    else:
        # Check for immediate friendly or opponent victories
        for r in range(3):
            for c in range(3):
                if not board[r][c]:
                    if checkVictory(board,r,c,side) or checkVictory(board,r,c,3-side):
                        return r,c
                    
        # Prevent future double-atacks
        tracking = [[0,0,0],[0,0,0],[0,0,0]]
        for R in range(3):
            for C in range(3):
                if not board[R][C]:
                    newBoard = deepcopy(board)
                    # Hypothetically place in spot
                    newBoard[R][C] = side
                    for r in range(3):
                        for c in range(3):
                            if not newBoard[r][c]:
                                newBoard2 = deepcopy(newBoard)
                                # Hypothetically place response
                                newBoard2[r][c] = 3-side
                                for r2 in range(3):
                                    for c2 in range(3):
                                        if not newBoard[r2][c2]:
                                            # Track possible victories after response
                                            if checkVictory(newBoard2,r2,c2,3-side):
                                                tracking[R][C] += 1
        for r in range(3):
            for c in range(3):
                if not board[r][c] and tracking[r][c]/2 < 2:
                    return r,c

        # Take what you can get!
        for r in range(3):
            for c in range(3):
                if not board[r][c]:
                    return r,c
                
        # Default to player input
        # print("Defaulting to player input...")
        # print(tracking)
        # return getValidPlayerInput(board)
    
victory = ''
firstTurn = 'Human'
secondTurn = 'CPU'
board = [[0,0,0],[0,0,0],[0,0,0]]

while 1:
    dispBoard(board)
    if firstTurn == 'Human':
        Y, X = getValidPlayerInput(board)
    else:
        Y, X = getCPUInput(board, 1)
    print('\n')
    board[Y][X] = 1
    if checkVictory(board,Y,X,1):
        victory = firstTurn
        break
    if not [x for y in board for x in y].count(0):
        break
    dispBoard(board)
    print('\n')
    if firstTurn == 'Human':
        Y, X = getCPUInput(board, 2)
    else:
        Y, X = getValidPlayerInput(board)
    board[Y][X] = 2
    if checkVictory(board,Y,X,2):
        victory = secondTurn
        break

print('\n\n'+(victory+' wins!' if victory else 'Tie!'))
dispBoard(board)
