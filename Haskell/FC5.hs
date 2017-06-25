import Data.List
factors n = filter (\x -> rem n x == 0) [2..(floor (sqrt (fromIntegral n)))]
findFactor n = if null (factors n) then n else head (factors n) 

fc5 n = fc5b [1] n

fc5b factors 1 = sort factors
fc5b factors n = fc5b (nub (concat (map (\x -> [x,x*factor]) factors))) (quot n factor)
	where factor = findFactor n
