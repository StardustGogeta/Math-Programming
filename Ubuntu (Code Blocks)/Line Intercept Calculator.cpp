#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
int main ()
{
double s,s2,y1,y2,x,y3,A,B,C,D,E,F,G,H;
cout<<"Enter coordinate pairs for two lines (0) or equations (1).\n";
bool r;
cin>>r;
if (r == false)
{
    cout<<"\nLine 1\n_________________________\nCoordinate Pair 1\nX: ";
    cin>>A;
    cout<<"Y: ";
    cin>>B;
    cout<<"Coordinate Pair 2\nX: ";
    cin>>C;
    cout<<"Y: ";
    cin>>D;
    cout<<"\nLine 2\n_________________________\nCoordinate Pair 1\nX: ";
    cin>>E;
    cout<<"Y: ";
    cin>>F;
    cout<<"Coordinate Pair 2\nX: ";
    cin>>G;
    cout<<"Y: ";
    cin>>H;
    s = (D-B)/(C-A);
    s2 = (H-F)/(G-E);
    y1 = B-(s*A);
    y2 = F-(s2*E);
}
else
{
    cout<<"\nSlope 1: ";
    cin>>s;
    cout<<"Y-Intercept 1: ";
    cin>>y1;
    cout<<"Slope 2: ";
    cin>>s2;
    cout<<"Y-Intercept 2: ";
    cin>>y2;
}
x=(y2-y1)/(s-s2);
y3=(s-s2)*x+y2;
cout<<"\nThe point of intersection is ("<<x<<","<<y3<<").";
}
