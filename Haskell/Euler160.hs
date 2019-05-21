-- This is a copy of the solution given here, with notes written by me:
-- https://github.com/nayuki/Project-Euler-solutions/blob/master/haskell/p160.hs?ts=4
-- See https://github.com/nayuki/Project-Euler-solutions/blob/master/java/p160.java
-- for notes by the original authors on why this works.

-- Solve the problem at hand:
main = putStrLn (show ans)
ans = f (10^12 :: Integer)

-- factorialSuffix
-- Returns the last five digits of n!.
-- This takes all the ignored factors of two
-- and multiplies them at the end, except the ones that match with fives to make tens.
f n = md $ (g n) * (2 ^ (mod ((c 2 n) - (c 5 n)) 2500))

-- factorialish
-- Multiplies the results of odd factorial and even factorial.
g n = md $ (ge n) * (go n)

-- evenFactorialish
-- Returns product of even numbers up to n, with all factors of 2 ignored. This equates to (n//2)!.
ge 0 = 1
ge n = g (div n 2)

-- oddFactorialish
-- Returns product of odd numbers up to n that are not divisible by 5.
go 0 = 1
go n = md $ (go (div n 5)) * (h n)

-- factorialCoprime
-- Returns the value (n % 10^5)! % 10^5, ignoring any factors divisible by 2 or 5.
h n = foldl (\x y -> md $ x * y) 1 $ filter (\k -> mod k 2 /= 0 && mod k 5 /= 0) [1..md n]

-- countFactors
-- Uses recursion to count the number of times m divides n!.
c n 0 = 0
c n m = (div m n) + (c n (div m n))

-- Takes the last five digits of a number.
md n = mod n (10^5)
