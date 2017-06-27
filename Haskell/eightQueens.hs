import Data.List

noDiags arr = nD (+) && nD (-)
	where nD op = (length (nub (map (\(x,y) -> op y x) (zip [1..8] arr)))) == 8

-- Returns the nth solution found for the eight queens problem (starting at 0)
eightQueens n = (filter noDiags (permutations [1..8])) !! n
