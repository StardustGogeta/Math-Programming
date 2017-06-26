import Math.Combinatorics.Exact.Binomial
-- Requires the "exact-combinatorics" package

coinFlip heads flips = (concat ["This combination occurs ",show (100*(fromIntegral (choose flips heads))/(fromIntegral (2^flips))),"% of the time."])
