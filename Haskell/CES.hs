-- (-2) 7 (-9) 0 (-10) (-5)
import Linear
import Control.Lens
roundTo x n = (fromIntegral (floor (x*10^n)))/10^n
ces :: V3 Double -> V3 Double -> V3 Double -> V3 Double -> V3 Double -> V3 Double -> IO ()
calc :: M33 Double -> IO ()
calc2 :: Double -> Double -> Double -> IO ()
ces a b c d e f = calc ((inv33 $ V3 (V3 a b 1)(V3 c d 1)(V3 e f 1)) !* (V3 (-a*a-b*b)(-c*c-d*d)(-e*e-f*f)))
calc m = calc2 (m^?!element 0^?!element 0) (m^?!element 1^?!element 0) (m^?!element 2^?!element 0)
calc2 d e f = putStrLn ("(x - "++show (roundTo (-d/2) 3)++")² + (y - "++show (roundTo (-e/2) 3)++")² = "++show (roundTo (-f+d^2/4+e^2/4) 3))