#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
    double pi = atan(1) * 4;
    string angleType;
    cout << "Degrees (d) or radians (r)?\n";
    cin >> angleType;
    double orig;
    cout << "What is the angle measure? (decimal)\n";
    cin >> orig;
    if (angleType == "d")
    {
        orig = orig * pi/180;
        cout << "sin θ = " << sin(orig) << endl;
        cout << "cos θ = " << cos(orig) << endl;
        cout << "tan θ = " << tan(orig) << endl;
        cout << "csc θ = " << 1/sin(orig) << endl;
        cout << "sec θ = " << 1/cos(orig) << endl;
        cout << "cot θ = " << 1/tan(orig) << endl;
    }
    else
    {
        bool radType;
        cout << "Is it in terms of pi? (Y=1)\n";
        cin >> radType;
        if (radType == true)
        {
            orig = pi * orig;
            cout << "sin θ = " << sin(orig) << endl;
            cout << "cos θ = " << cos(orig) << endl;
            cout << "tan θ = " << tan(orig) << endl;
            cout << "csc θ = " << 1/sin(orig) << endl;
            cout << "sec θ = " << 1/cos(orig) << endl;
            cout << "cot θ = " << 1/tan(orig) << endl;
        }
        else
        {
            cout << "sin θ = " << sin(orig) << endl;
            cout << "cos θ = " << cos(orig) << endl;
            cout << "tan θ = " << tan(orig) << endl;
            cout << "csc θ = " << 1/sin(orig) << endl;
            cout << "sec θ = " << 1/cos(orig) << endl;
            cout << "cot θ = " << 1/tan(orig) << endl;
        }
    }
    return 0;
}
