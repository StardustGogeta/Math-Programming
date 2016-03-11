#include <stdio.h>
#include <math.h>

void main()
{
    long n;
	printf("What is your number?\n");
	scanf("%ld",n);
	printf(n);
	if (n)
	{
	    long d;
		for (d=1; d<sqrt(n); d++)
		{
			if (n % d == 0)
			{
				printf("%d, %d\n",n/d,d);
			}
		}
		printf("\nThe list of factors has been successfully generated.\n");
	}
	else
	{
		printf("Sorry, I can't do that.\n");
	}
}
