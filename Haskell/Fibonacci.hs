fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
fib x = fibs !! x