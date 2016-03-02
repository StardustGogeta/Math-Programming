#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
int main ()
{
cout<<"What is the number?\n";
long fN;
cin>>fN;
cout<<"What is the current base? (1 < x < 11)\n";
int fB;
cin>>fB;
cout<<"What is the desired base? (1 < x < 11)\n";
int sB;
cin>>sB;
if (fB>10 or fB<2 or sB>10 or sB<2)
{
    cout<<"\nStop wasting time.\n";
}
else
{
    long C;
    long d=0;
    long tV;
    long tVT=0;
    long dV=1;
    long dP;
    while(fN>0)
    {
        C=fN;
        d=floor(log10(C));
        C/=pow(10,d);
        dP=pow(10,d);
        dV=pow (fB,d);
        tV=C*dV;
        fN-=C*dP;
        tVT+=tV;
    }
    long tVTN;
    long sN=0;
    while(tVTN>0)
    {
        long sP=pow(sB,floor(log10(tVT)/log10(sB)));
        dV=pow(10,floor(log10(tVT)/log10(sB)));
        tVTN=tVT%sP;
        sN+=(tVT-tVTN)*dV/sP;
        tVT=tVTN;
    }
    cout<<"Your number is "<<sN<<".";
}
}
