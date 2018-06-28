pairs = zip <*> tail
-- Implicit list argument
-- See https://stackoverflow.com/a/4506000/5732397 for explanation of `<*>` operator

row :: Num a => ((a, a) -> a) -> Integer -> [[a]]
row func 0 = [[1]]
row func n = concat [prevRows, [map func (pairs (0:(last prevRows)++[0]))]]
    where prevRows = (row func (n-1))

pascalTriangle :: Integer -> [[Integer]]
pascalTriangle n = row (uncurry (+)) n

customTriangle :: Num a => ((a, a) -> a) -> Integer -> [[a]]
customTriangle customFunc n = row customFunc n

prettyPrint triangle = putStr (unlines (map show triangle))
