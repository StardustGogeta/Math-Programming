#include <stdio.h>
#include <stdlib.h>

void main()
{
	// -2 7 -9 0 -10 -5
	puts("Enter your three coordinate points, separated by spaces.");
	double a,b,c,d,e,f,D,E,F;
	int i,o;
	scanf("%lf %lf %lf %lf %lf %lf",&a,&b,&c,&d,&e,&f);
	double *m[3];
	for(i=0;i<3;i++) m[i] = (double *)malloc(sizeof(double));
	*m[0] = -a*a-b*b;
	*m[1] = -c*c-d*d;
	*m[2] = -e*e-f*f;
	double *m2[3];
	for(i=0;i<3;i++) m2[i] = (double *)malloc(3*sizeof(double));
	m2[0][0] = d-f; m2[0][1] = f-b; m2[0][2] = b-d;
	m2[1][0] = e-c; m2[1][1] = a-e; m2[1][2] = c-a;
	m2[2][0] = c*f-d*e; m2[2][1] = b*e-a*f; m2[2][2] = a*d-b*c;
	for (i=0;i<3;i++)
		for (o=0;o<3;o++)
			m2[i][o]/=(a*d-a*f-b*c+b*e+c*f-d*e);
	double *DEF[3];
	for(i=0;i<3;i++) DEF[i] = (double *)malloc(sizeof(double));
	for(i=0;i<3;i++)
		*DEF[i] = *m[0]*m2[i][0]+*m[1]*m2[i][1]+*m[2]*m2[i][2];
	D=*DEF[0]/-2,E=*DEF[1]/-2,F=*DEF[2];
	char A=253;
	printf("(x - %.3lf)%c + (y - %.3lf)%c = %.3lf",D,A,E,A,-F+D*D+E*E);
}
