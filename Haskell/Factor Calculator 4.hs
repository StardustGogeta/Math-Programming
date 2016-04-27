fc4 :: Integer -> [IO ()]
check :: Integer -> Double -> IO ()
fc4 input = map (check input) [1 .. sqrt (fromIntegral input)]
check input divisor = if (fromIntegral input/divisor==0) then print(divisor, fromIntegral input/divisor) else print()