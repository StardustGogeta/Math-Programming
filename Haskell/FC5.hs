import Data.List
factors n = filter (\x -> rem n x == 0) [2..(floor (sqrt (fromIntegral n)))]
findFactor n = if null (factors n) then n else head (factors n) 

fc5 n = f [1] n
	where
		f factors 1 = sort factors
		f factors n = f (nub (concatMap (\x -> [x,x*factor]) factors)) (quot n factor)
			where factor = findFactor n
