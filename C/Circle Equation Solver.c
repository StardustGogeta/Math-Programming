#include <stdio.h>
#include <stdlib.h>

void main() {
	// -2 7 -9 0 -10 -5
	puts("Enter your three coordinate points, separated by spaces.");
	double a,b,c,d,e,f,h,k,r2;
	scanf("%lf %lf %lf %lf %lf %lf",&a,&b,&c,&d,&e,&f);
	double x0 = (a+c)/2,
			y0 = (b+d)/2,
			x1 = (a+e)/2,
			y1 = (b+f)/2,
			s = (a-c)/(d-b),
			s2 = (a-e)/(f-b);
	h = (y1-y0+s*x0-s2*x1) / (s-s2);
	k = (h-x0)*s+y0;
	r2 = (h-a)*(h-a)+(k-b)*(k-b);
	char A=253;
	printf("(x - %.3lf)%c + (y - %.3lf)%c = %.3lf",h,A,k,A,r2);
}
