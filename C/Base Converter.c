#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void main()
{
	char *fN = (char*) malloc(500);
    int fB; int sB;
	puts("What is the number?");
	scanf("%s",fN);
	puts("What is the current base? (<=36)");
	scanf("%d",&fB);
	puts("What is the desired base? (<=10)");
	scanf("%d",&sB);
	if (1<fB<37 && 1<sB<11)
	{
		long tVT = strtol(fN,NULL,fB);
		char *sN = (char*) malloc(500);
		char *test = (char*) malloc(500);
		while (tVT)
		{
            sprintf(test,"%d",tVT%sB);
            strcat(test,sN);
            strcpy(sN,test);
            tVT/=sB;
		}
		printf("\nYour number is %s.\n",sN);
	}
	else
		puts("\nStop wasting time.");
}
