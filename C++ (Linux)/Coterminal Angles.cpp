#include <stdio.h>
#include <cmath>
#include <iostream>
using namespace std;

int main ()
{
    cout << "Please state an angle.\n";
    int orig;
    cin >> orig;
    int ang1 = orig;
    int ang2 = orig;
    if (orig > 0)
    {
        if (orig > 360)
        {
            while (ang1 > 360)
            {
                ang1 -= 360;
            }
            ang2 = ang1 - 360;
        }
        else
        {
            ang1 += 360;
            ang2 -= 360;
        }
    }
    else
    {
        if (orig < -360)
        {
            while (ang1 < -360)
            {
                ang1 += 360;
            }
            ang2 = ang1 + 360;
        }
        else
        {
            ang1 -= 360;
            ang2 += 360;
        }
    }
    cout << "\nThe coterminal angles are " << ang1 << " and " << ang2 << ".\n";
}
