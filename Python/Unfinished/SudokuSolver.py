def dispGrid(grid,n=1):
##      for x in range(9):
##          print(grid[y][x],end = "    " if x%3==2 else "  ")
        print("\n".join(["  ".join([str(x) for x in grid[y]]) for y in range(9)])+"\n"*n)
        #print("\n" if y%3==2 else "")

def sumGrid(grid):
    return sum([x for y in grid for x in y])

# www.websudoku.com/?level=1&set_id=10186372013
##puzzle = [  [8,6,0,0,2,0,0,1,4],
##            [0,0,0,0,8,0,0,6,0],
##            [0,3,0,0,1,7,9,0,8],
##	    [7,0,0,0,0,0,2,3,0],
##	    [0,0,6,3,5,1,8,0,0],
##	    [0,8,3,0,0,0,0,0,6],
##	    [6,0,8,2,3,0,0,7,0],
##	    [0,1,0,0,9,0,0,0,0],
##	    [5,7,0,0,4,0,0,2,3]]

# www.websudoku.com/?level=1&set_id=2278555519
##puzzle = [  [0,5,0,2,3,4,0,0,0],
##            [0,0,0,8,0,0,0,1,0],
##            [7,0,6,0,0,0,2,0,3],
##	    [5,0,0,0,2,9,0,4,8],
##	    [8,0,4,0,0,0,9,0,5],
##	    [6,9,0,4,5,0,0,0,7],
##	    [3,0,5,0,0,0,8,0,1],
##	    [0,2,0,0,0,6,0,0,0],
##	    [0,0,0,3,1,5,0,6,0]]

# www.websudoku.com/?level=2&set_id=738252358
##puzzle = [  [9,1,0,0,2,0,4,7,0],
##            [0,0,4,0,3,0,0,6,1],
##            [0,5,0,0,0,0,0,9,0],
##	    [0,0,0,2,0,0,7,5,9],
##	    [0,0,0,0,7,0,0,0,0],
##	    [4,9,7,0,0,6,0,0,0],
##	    [0,4,0,0,0,0,0,2,0],
##	    [2,7,0,0,5,0,8,0,0],
##	    [0,8,3,0,9,0,0,4,5]]

# www.websudoku.com/?level=3&set_id=833928262
##puzzle = [  [9,0,1,8,0,0,0,0,0],
##            [0,0,4,3,0,0,0,0,0],
##            [2,0,0,0,4,6,0,0,0],
##	    [0,0,7,2,1,0,3,0,0],
##	    [0,3,0,5,0,7,0,2,0],
##	    [0,0,9,0,8,3,6,0,0],
##	    [0,0,0,7,2,0,0,0,5],
##	    [0,0,0,0,0,1,4,0,0],
##	    [0,0,0,0,0,8,2,0,6]]

# www.websudoku.com/?level=4&set_id=1321627164
puzzle = [  [0,0,8,0,0,9,0,0,0],
            [0,1,0,0,0,0,0,7,0],
            [7,0,5,0,3,0,2,0,0],
	    [0,4,3,0,5,0,0,0,7],
	    [0,0,1,0,0,0,6,0,0],
	    [5,0,0,0,8,0,3,4,0],
	    [0,0,6,0,2,0,5,0,4],
	    [0,3,0,0,0,0,0,9,0],
	    [0,0,0,9,0,0,7,0,0]]

##puzzle = [  [1,2,3,4,5,6,7,8,9],
##            [1,2,3,4,5,6,7,8,9],
##            [1,2,3,4,5,6,7,8,9],
##            [1,2,3,4,5,6,7,8,9],
##            [1,2,3,4,5,6,7,8,9],
##            [1,2,3,4,5,6,7,8,9],
##            [1,2,3,4,5,6,7,8,9],
##            [1,2,3,4,5,6,7,8,9],
##            [1,2,3,4,5,6,7,8,9]]

dispGrid(puzzle);
while (sumGrid(puzzle) < 405):
    pointingRows = []
    pointingColumns = []
    for item in range(1,10):
        rows = [y for y in range(9) if not item in puzzle[y]]
        if not rows: continue
        columns = [x for x in range(9) if not item in [puzzle[y][x] for y in range(9)]]
        bigs = [x for x in range(9) if not item in [y for x in (puzzle[x-x%3+o][(x*3)%9:(x*3)%9+3] for o in range(3)) for y in x]]

        print("init",item,rows,columns,bigs)
##        for y in range(9):
##            for x in range(9):
##                print("box",y-y%3+int(x/3))

        
        for y in rows: # Checking if only one spot left in a row.
            poss = [x for x in range(9) if not puzzle[y][x] and x in columns and y-y%3+int(x/3) in bigs]
            if len(poss) == 1:
                print(item,y,poss)
                puzzle[y][poss[0]] = item
                rows = [y for y in range(9) if not item in puzzle[y]]
                columns = [x for x in range(9) if not item in [puzzle[y][x] for y in range(9)]]
                bigs = [x for x in range(9) if not item in [y for x in (puzzle[x-x%3+o][(x*3)%9:(x*3)%9+3] for o in range(3)) for y in x]]
                print("row")
                dispGrid(puzzle)
                continue
            if int(poss[-1]/3)==int(poss[0]/3): # Checking for pointing pairs and triplets.
                pointingRows += [y-y%3+int(poss[0]/3)] + [item] + [y]
                
                
        for x in columns: # Checking if only one spot left in a column.
            poss = [y for y in range(9) if not puzzle[y][x] and y in rows and y-y%3+int(x/3) in bigs]
            if len(poss) == 1:
                print(item,x,poss)
                puzzle[poss[0]][x] = item
                rows = [y for y in range(9) if not item in puzzle[y]]
                columns = [x for x in range(9) if not item in [puzzle[y][x] for y in range(9)]]
                bigs = [x for x in range(9) if not item in [y for x in (puzzle[x-x%3+o][(x*3)%9:(x*3)%9+3] for o in range(3)) for y in x]]
                print("column")
                dispGrid(puzzle)
            if poss[-1]-poss[-1]%3==poss[0]-poss[0]%3: # Checking for pointing pairs and triplets.
                pointingColumns += [poss[0]-poss[0]%3+int(x/3)] + [item] + [x]
                
        for x in range(9): # Checking if only one spot left in a box.
            eligible = []
            if x not in bigs:
                continue
            for zero in range(9):
                #print(zero,int(zero/3)+x-x%3,zero%3+(x*3)%9)
                if puzzle[int(zero/3)+x-x%3][zero%3+(x*3)%9] == 0 and (int(zero/3) + x-x%3) in rows and (zero%3 + (x*3)%9) in columns:
                    eligible += [zero]
            if len(eligible) == 1:
                zero = eligible[0]
                puzzle[int(zero/3)+x-x%3][zero%3+(x*3)%9] = item
                rows = [y for y in range(9) if not item in puzzle[y]]
                columns = [x for x in range(9) if not item in [puzzle[y][x] for y in range(9)]]
                bigs = [x for x in range(9) if not item in [y for x in (puzzle[x-x%3+o][(x*3)%9:(x*3)%9+3] for o in range(3)) for y in x]]
                print("box")
                dispGrid(puzzle)

    print("point",pointingRows,pointingColumns,item)
    for y in range(9): # Checking to see if there are any single candidates.
        for x in range(9):
            if not puzzle[y][x]:
                a = y-y%3+int(x/3) # Setting the large box.
                row = puzzle[y]
                column = [puzzle[a][x] for a in range(9)]
                box = [y for x in (puzzle[a-a%3+o][(a*3)%9:(a*3)%9+3] for o in range(3)) for y in x]
                pointing = []
                for b in range(0,len(pointingRows),3):
                    if a == pointingRows[b] and y != pointingRows[b+2]:
                        pointing += [pointingRows[b+1]]
                for b in range(0,len(pointingColumns),3):
                    if a == pointingColumns[b] and x != pointingColumns[b+2]:
                        pointing += [pointingColumns[b+1]]
                nums = set(row+column+box+pointing)
                print("test",y,x,nums,pointing)
                if len(nums) == 9:
                    for n in range(1,10):
                        if not n in nums:
                            puzzle[y][x] = n
                            break
                    print("single candidate",y,x,puzzle[y][x],nums)
                    dispGrid(puzzle)
            


    #break

print("\nFinal solution:")
dispGrid(puzzle);
