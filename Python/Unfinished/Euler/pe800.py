
import math
import common_util
from math import ceil, log, log2

# We want all integers of the form p^q * q^p below a certain threshold
# If p^q * q^p <= M^M
# then q*log(p) + p*log(q) <= M*log(M)

# Suppose p >= 2. We want to find the largest q possible (Q) for p = 2
# and so then we can bound a prime search with that Q as the max.
# We know 2^q * q^2 > 2^q, so we can set Q = log_2(M^M) as a conservative estimate.

M = 800800

Q = ceil(M * log2(M))

primes = common_util.efficientSieve(Q)

p_index = 0
q_index = len(primes) - 1

total = 0
while p_index < q_index:
    p = primes[p_index]
    q = primes[q_index]
    if q * log(p) + p * log(q) <= M * log(M):
        # This is a valid hybrid integer, and so are all with q down to p-1 for this p
        total += q_index - p_index
        p_index += 1
    else:
        q_index -= 1
print(total)
        
