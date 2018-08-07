import Data.List
import Data.List.Split

p01 = last

p02 = head . tail . reverse

p03 ls n = ls !! (n-1)

p04 ls = length ls

p05 = reverse

p06 ls = ls == reverse ls

-- p07 skipped

p08 :: String -> String
p08 = map head . group

p09 :: String -> [String]
p09 = group

p10 :: String -> [(Int, Char)]
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


