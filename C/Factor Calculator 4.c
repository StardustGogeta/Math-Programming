#include <stdio.h>
#include <math.h>

void main()
{
    long long n;
	puts("What is your number?");
	scanf("%lld",&n);
	if (n>0)
	{
	    long long d;
		for (d=1; d<=sqrt(n); d++)
			if (n % d == 0)
				printf("%lld, %lld\n",n/d,d);
		puts("\nThe list of factors has been successfully generated.");
	}
	else
		puts("\nSorry, I can't do that.");
}
