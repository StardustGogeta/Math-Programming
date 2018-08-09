import Data.List
import Data.List.Split
import Data.Function
import Data.Bits

p01 :: [a] -> a
p01 = last

p02 :: [a] -> a
p02 = head . tail . reverse

p03 :: [a] -> Int -> a
p03 ls n = ls !! (n-1)

p04 :: [a] -> Int
p04 ls = length ls

p05 :: [a] -> [a]
p05 = reverse

p06 :: Eq a => [a] -> Bool
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
p22 = enumFromTo

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
p33 = ((1 ==) .) . gcd

p34 :: Integral a => a -> Int
p34 n = length $ filter (p33 n) [1..n]

p35 :: Integral a => a -> [a]
p35 n = if n == 1 then [] else let f = findFactor n in f : p35 (n `div` f)
    where findFactor n = head $ filter ((0 ==) . (mod n))  [2..]

p36 :: Integral a => a -> [(a, Int)]
p36 = let pair ls = (head ls, length ls) in map pair . group . p35

p37 :: Int -> Int
p37 = product . map (\(x,y) -> (x-1)*x^(y-1)) . p36

-- p38 := p37 is much faster than p34, for obvious reasons

p39 :: (Integral a, Enum a) => a -> a -> [a]
p39 = (filter p31 .) . enumFromTo

p40 :: (Integral a, Enum a) => a -> (a, a)
p40 n = head $ filter (\(_,y) -> p31 y) $ map (\x -> (x, n-x)) $ p39 0 n

p41a :: (Integral a, Enum a) => a -> a -> [(a, a)]
p41a = (map p40 .) . (filter ((0 ==) . (`mod` 2)) .) . enumFromTo

p41b :: (Integral a, Enum a) => a -> a -> a -> [(a, a)]
p41b a b n = filter (\(x,y) -> x > n && y > n) $ p41a a b

-- p42, p43, p44, and p45 do not exist

and' :: Bool -> Bool -> Bool
and' = (&&)
or' :: Bool -> Bool -> Bool
or' = (||)
nand' :: Bool -> Bool -> Bool
nand' = (not .) . (&&)
nor' :: Bool -> Bool -> Bool
nor' = (not .) . (||)
xor' :: Bool -> Bool -> Bool
xor' = (/=)
impl' :: Bool -> Bool -> Bool
impl' = (&&) -- Not implemented
equ' :: Bool -> Bool -> Bool
equ' = (==)
infixr 3 `and'`, `nand'`
infixr 2 `or'`, `nor'`
infixr 1 `impl'`, `equ'`, `xor'`

-- Taken from https://stackoverflow.com/a/1959734/5732397 --
decToBin :: Int -> [Bool]
decToBin x = reverse $ map (\y -> x .&. y > 0) (map (2^) [0..floor $ logBase 2 $ fromIntegral x])
decToBinFixedLen :: Int -> Int -> [Bool]
decToBinFixedLen len x = reverse $ map (\y -> x .&. y > 0) (map (2^) [0..len-1])

-- This has been generalized to n arguments, provide as a list in a lambda for f
p46 :: Int -> ([Bool] -> Bool) -> IO ()
p46 n f = sequence_ (map printLn (map (decToBinFixedLen n) [0..2^n-1]))
    where
        printLn arr = putStrLn (show $ arr ++ [f arr])

-- p47 and p48 are completed by the function p46 above

-- A gray code is one where it is n-digits wide and n+1 strings long
-- Each new layer has the old one with zeros overlaid, then the reversed old with ones overlaid
p49 :: Integral a => a -> [String]
p49 1 = ["0", "1"]
p49 n = map ('0':) (gray (n-1)) ++ map ('1':) (reverse $ gray (n-1))
