import Data.List
fc4 a = sort (concatMap (\x -> [x, div a x]) (filter (\x -> rem a x == 0) [1..(floor (sqrt (fromIntegral a)))]))
