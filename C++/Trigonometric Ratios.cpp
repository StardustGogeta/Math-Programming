#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
	long double rad, o, pi = atan(1)*4, deg;
	cout << "Degrees (0) or radians (1)?\n";
	cin >> deg;
	cout << "What is the angle measure?\n";
	cin >> o;
	if (deg)
	{
		cout << "Is it in terms of pi? (Y=1)\n";
		cin >> rad;
		if (rad)
			o *= pi;
	}
	else
		o *= pi/180;
	printf("\nsin = %Lf\ncos = %Lf\ntan = %llf\ncsc = %llf\nsec = %llf\ncot = %llf\n",sin(o),cos(o),tan(o),1/sin(o),1/cos(o),1/tan(o));
}
