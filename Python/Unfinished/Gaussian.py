isPrime = lambda x: all (x%d for d in range(2, int(x**.5)+1))
isGPrime = lambda r,i: (isPrime(r**2+i**2) and (r**2+i**2)%1==0 if (r!=0 and i!=0) else (i%4==3 if r==0 else r%4==3))
