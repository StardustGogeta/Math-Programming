import Data.List
fc4 a = sort (concat (map (\x -> [x, div a x]) (filter (\x -> rem a x == 0) [1..(floor (sqrt (fromIntegral a)))])))
