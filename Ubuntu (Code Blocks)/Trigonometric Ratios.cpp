#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
int main ()
{
    double rad,o,pi=atan(1)*4,angle;
    cout<<"Degrees (0) or radians (1)?\n";
    cin>>angle;
    cout<<"What is the angle measure?\n";
    cin>>o;
    if (angle==0)
    {
        o=o*pi/180;
    }
    else
    {
        cout<<"Is it in terms of pi? (Y=1)\n";
        cin>>rad;
        if (rad==1)
        {
            o=pi*o;
        }
    }
    cout<<"sin = "<<sin(o)<<"\ncos = "<<cos(o)<<"\ntan = "<<tan(o)<<"\ncsc = "<<1/sin(o)<<"\nsec = "<<1/cos(o)<<"\ncot = "<<1/tan(o)<<endl;
}
