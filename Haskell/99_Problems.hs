import Data.List
import Data.List.Split
import Data.Function

p01 = last

p02 = head . tail . reverse

p03 ls n = ls !! (n-1)

p04 ls = length ls

p05 = reverse

p06 ls = ls == reverse ls

-- p07 skipped

p08 :: Eq a => [a] -> [a]
p08 = map head . group

p09 :: Eq a => [a] -> [[a]]
p09 = group

p10 :: Eq a => [a] -> [(Int, a)]
p10 = map enc . group
    where enc s = (length s, head s)
    
data ItemCount = Single Char | Multiple Int Char deriving (Show, Read)
p11 :: String -> [ItemCount]
p11 = map enc . group
    where enc s = case length s of 1 -> Single $ head s
                                   otherwise -> Multiple (length s) (head s)
                                   
p12 :: [ItemCount] -> String
p12 = concatMap dec
    where dec (Multiple n c) = replicate n c
          dec (Single c) = [c]

-- p13 skipped
p14 :: [a] -> [a]
p14 = concatMap (\x -> [x,x])

p15 :: [a] -> Int -> [a]
p15 s n = concatMap (replicate n) s

p16 :: [a] -> Int -> [a]
--p16 = concatMap init . flip chunksOf
p16 ls n = concatMap (take $ n-1) $ chunksOf n ls

p17 :: [a] -> Int -> ([a], [a])
p17 s n = (take n s, drop n s)

p18 :: [a] -> Int -> Int -> [a]
p18 ls n n2 = take (n2-n) $ drop n ls -- Intentionally dropping first character, change n to n-1 to fix

p19 :: [a] -> Int -> [a]
p19 ls n = take (length ls) $ drop (length ls + n) $ cycle ls

p20 :: Int -> [a] -> (a, [a])
p20 n ls = (ls !! n, take n ls ++ drop (n+1) ls) -- Intentionally off-by-one

p21 :: a -> [a] -> Int -> [a]
p21 a ls n = take n ls ++ a : drop n ls -- Intentionally off-by-one

p22 :: Enum a => a -> a -> [a]
p22 a b = [a..b]

-- p23 skipped
-- p24 skipped
-- p25 skipped

p26 :: Int -> [a] -> [[a]]
p26 n ls = filter ((== n) . length) $ subsequences ls

-- p27 skipped

p28a :: [[a]] -> [[a]]
p28a = sortBy (compare `on` length)

p28b :: [[a]] -> [[a]]
p28b = concat . p28a . groupBy ((==) `on` length) . p28a

-- p29 and p30 do not exist

p31 :: Integral a => a -> Bool
p31 n = if n < 2 then False else let md x = mod n x /= 0 in all md [2..floor $ sqrt $ fromIntegral n]

p32 :: Integral a => a -> a -> a
p32 = gcd

p33 :: Integral a => a -> a -> Bool
p33 a b = (1 == ) $ gcd a b

p34 :: Integral a => a -> Int
p34 n = length $ filter (p33 n) [1..n]


