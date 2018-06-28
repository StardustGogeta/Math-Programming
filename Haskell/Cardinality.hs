-- The following functions show that each of the sequences has
-- cardinality aleph-null due to a direct mapping from the natural numbers.

alephNull_evenIntegers x
                       | mod x 2 == 0 = x
                       | otherwise = -(x+1)

alephNull_oddIntegers x
                       | mod x 2 == 1 = x
                       | otherwise = -(x+1)
