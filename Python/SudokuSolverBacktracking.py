# This is different from the other `SudokuSolver.py` file because this uses backtracking and recursion
# rather than actually trying to solve the board like a human would.

class Board:
    def __init__(self, fill = None):
        self.arr = [list(0 for _ in range(9)) for _ in range(9)]
        if fill:
            self.fill(fill)

    @staticmethod
    def getBoxNum(i, j): # Gets the corresponding mini-grid number for a given coordinate pair on the board
        return (i // 3) * 3 + j // 3

    def findNext(self): # Returns coords of next open spot as 2-tuple
        for i in range(9):
            for j in range(9):
                if not self.arr[i][j]:
                    return (i, j)

    def fill(self, arr): # Fill the board using an 81-element list
        for i in range(9):
            for j in range(9):
                # print(i * 9 + j)
                self.arr[i][j] = arr[i * 9 + j]

    def set(self, i, j, val): # Place an element into the board
        self.arr[i][j] = val

    def getAll(self): # Dump all elements of the board
        return [elem for row in self.arr for elem in row]

    def getBox(self, box): # Get the box of nine squares in a region of the board
        return [elem for i in range((box // 3) * 3, (box // 3) * 3 + 3) for elem in self.arr[i][(box % 3) * 3 : (box % 3) * 3 + 3]]

    def valid(self, coords = None): # Return whether the board is valid or not, optionally in a specific row and column
        if coords is None:
            for row in self.arr:
                if len(set(row)) != 9:
                    return False
            for j in range(9):
                if len(set(self.arr[i][j] for i in range(9))) != 9:
                    return False
            for box in range(9):
                if not self.validBox(box):
                    return False
            return True
        return validSet(self.arr[coords[0]]) and validSet(self.arr[i][coords[1]] for i in range(9)) and self.validBox(Board.getBoxNum(*coords))

    def validBox(self, box):
        return validSet(self.getBox(box))

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.arr)

def validSet(row): # Checks for 1 through 9 without duplicates
    noZeros = [elem for elem in row if elem]
    return len(noZeros) == len(set(noZeros))

def solve(board): # Solves a Board object
    coords = board.findNext()
    if not coords: # If all spots are filled, return the board if and only if it is valid
        if board.valid():
            return board
        return False # Otherwise, fail
    for val in range(1, 10): # Iterate through all possible values in the first empty space
        board.set(*coords, val) # Set the value
        if board.valid(coords): # Check if the row, column, or mini-grid have duplicate entries
            sol = solve(board) # Solve the rest of the board
            if sol: # If the board had a solution with this entry, return it
                return sol
    # If there were no solutions at all with this branch, an error was made previously, and we must backtrack
    board.set(*coords, 0) # Reset the altered location
    return False # Indicate no solutions

sample = [0, 6, 5, 7, 4, 2, 0, 9, 0,
                  0, 0, 9, 0, 0, 6, 5, 3, 4,
                  0, 0, 0, 0, 9, 0, 7, 0, 0,
                  9, 0, 0, 0, 0, 0, 8, 5, 3,
                  0, 0, 0, 8, 0, 9, 0, 0, 0,
                  8, 5, 2, 0, 0, 0, 0, 0, 6,
                  0, 0, 3, 0, 1, 0, 0, 0, 0,
                  6, 8, 1, 5, 0, 0, 3, 0, 0,
                  0, 9, 0, 6, 2, 3, 4, 8, 0]

sudoku = Board()
sudoku.fill(sample)
print(solve(sudoku))


