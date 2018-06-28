import Data.List
import qualified Data.Text as Text
import Data.Number.CReal
-- Solutions start with "pe", auxiliary functions end with "z"

main :: IO ()
main = putStrLn (show (pe160 1000000000000))
fibs :: [Integer]
findPrime :: Integer -> Integer -> Integer
pe1 :: Integer -> Integer
pe2 :: Integer -> Integer
pe3 :: Integer -> Integer
pe34 :: Integer
pe40 :: Integer
pe52 :: Integer -> Integer
pe52z :: Integer -> Integer -> Integer
pe57 :: Integer -> Integer
pe57z :: Integer -> Integer -> Integer -> Integer -> Integer
pe71 :: Integer -> (Integer, Integer)
pe71z :: Integer -> Integer -> Integer -> (Integer, Integer)
pe80 :: CReal -> CReal
pe92 :: Integer -> Integer
pe92z :: Integer -> Bool
pe99 :: IO()
pe99z :: [Text.Text] -> Double -> Double -> Double -> Double
pe160 :: Integer -> Integer
pe160y :: Integer -> Integer -> Integer -> Integer
pe160z :: Integer -> Integer

fibs = 0 : 1 : zipWith (+) fibs (tail fibs) -- Fibonacci sequence
findPrime a b = if (mod a b == 0) -- Finds smallest prime factor of a, starting at b
					then b
					else if b > (floor (sqrt (fromIntegral a)))
						then a
						else findPrime a (b+1)

pe1 a = sum [3,6..a-1] + sum [5,10..a-1] - sum [15,30..a-1] -- Input threshold value
pe2 a = sum (filter (\x -> mod x 2 == 0) (takeWhile (<= a) fibs)) -- Input threshold value
pe3 a = if (findPrime a 2) < a then pe3 (quot a (findPrime a 2)) else (findPrime a 2) -- Input number

-- EXPLANATION: 1 million is an approximate maximum
pe34 = sum (filter (\x -> x == sum (map (\y -> product [1..(read [y])]) (show x))) [10..1000000])

pe40 = product (map (\y -> read [(concat (map (\x -> show x) [1..1000000]))!!(10^y-1)]) [1,2,3,4,5,6])

pe52 a = pe52z a a -- Input number of multiples
pe52z a b = if toInteger (length (filter (== sort (show a)) (map (\x -> sort (show (x * a))) [1..b]))) == b then a else pe52z (a + 1) b

-- EXPLANATION: a/b will always go to (a+2b)/(a+b)
pe57 a = pe57z 3 2 a 0 -- Input number of expansions
pe57z a b c d = if c > 0
					then pe57z (a + (b * 2)) (a + b)
					(c - 1) (d + (if length (show a) > length (show b) then 1 else 0))
				else d

pe71 a = pe71z 1 1 a -- Input threshold
pe71z a b c = if a > c
				then (quot (floor (fromIntegral b*3/7)) (gcd b (floor (fromIntegral b*3/7))), quot b (gcd b (floor (fromIntegral b*3/7))))
				else pe71z	(a + 1)
							(if (3/7 - (fromIntegral (floor ((fromIntegral a)*3/7))/(fromIntegral a))) < (3/7 - (fromIntegral (floor ((fromIntegral b)*3/7))/(fromIntegral b))) && (a /= 3) && (3/7 > (fromIntegral (floor ((fromIntegral a)*3/7))/(fromIntegral a))) then a else b)
							c
				
pe80 a = sum (map (\x -> if sqrt x /= fromIntegral (floor (sqrt x)) then sum (map (\x -> read [x]) (show (floor((10^99) * (sqrt x) :: CReal)))) else 0) [1..a]) -- Input threshold value

pe92 a = toInteger (length (filter pe92z [1..a])) -- Input threshold
pe92z a
	| a == 1 = False
	| a == 89 = True
	| otherwise = pe92z (sum (map (\x -> (read [x])^2) (show a)))
		

-- EXPLANATION: All numbers can be reduced to e^x, with the largest x being the largest power
pe99 = do
		a <- readFile "p099_base_exp.txt"
		putStrLn (show (pe99z (Text.split (\x -> x==','||x=='\n') (Text.pack a)) 999 0 0))
pe99z a b c d = if b > 0
				then do
					let n = read (Text.unpack (a!!(floor(2*b))))
					let m = read (Text.unpack (a!!(floor(2*b+1))))
					pe99z a (b-1) (if (log n) * m > d
									then (b+1)
									else c)
								  (if (log n) * m > d
									then (log n) * m
									else d)
				else c

pe160 a = pe160y 1 1 a -- Input threshold  accumulator,tracker,limit
pe160y a b c
	| b <= c = pe160y ((mod . pe160z $! a * b) 100000) (b + 1) c
	| otherwise = a
pe160z a
	| rem a 10 == 0 = pe160z $! quot a 10
	| otherwise = a
	
	
	
{-pe160 a = mod (pe160z p) 100000 -- Input threshold
	where p = product (map pe160z [1..a])
pe160z a
	| mod a 10 == 0 = pe160z (quot a 10)
	| otherwise = a
	-}