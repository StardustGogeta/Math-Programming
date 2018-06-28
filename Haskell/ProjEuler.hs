import Data.List

--pe160 :: Integer -> Integer
pe160 :: Integer
pe160z :: Integer -> Integer

--pe160 a =  ((rem (pe160z (product (map pe160z [1..1000000]))) 1000000) ^ (a)) --100000
pe160 =  quot ((product [1..100000]) ^ (10^7)) 10^24999999997 `rem` 100000
--pe160 a = rem ((pe160z (foldl' (\x y -> rem (pe160z (x * y)) 100000) 1 (map pe160z [1..100000]))) ^ (a+1)) 100000	-- Input power of ten (above 5)
pe160z a = if rem a 10 == 0 then pe160z $! quot a 10 else a