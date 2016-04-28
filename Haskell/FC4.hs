import Control.Monad
fc4 a = check a (floor (sqrt (fromIntegral a)))
check a b = when (rem a b == 0) (print (div a b, b)) >> if b > 1 then check a (b-1) else putStrLn ("Done.")