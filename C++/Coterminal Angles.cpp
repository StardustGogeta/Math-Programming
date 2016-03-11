#include <stdio.h>
#include <cmath>
#include <iostream>
using namespace std;

int main()
{
	cout << "State an angle.\n";
	__int64 o;
	cin >> o;
	__int64 ang1=o, ang2=o;
    if (o>360)
    {
        while (ang1>360)
            ang1 -= 360;
        ang2 = ang1-360;
	}
	else if (o<-360)
    {
        while (ang1 < -360)
            ang1 += 360;
        ang2 = ang1+360;
    }
    else
    {
        ang1 -= 360;
        ang2 += 360;
    }
	cout << "\nCoterminal angles include " << ang1 << " and " << ang2 << ".\n";
}
