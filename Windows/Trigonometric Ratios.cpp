// Trigonometry.cpp : Defines the entry point for the console application.
//

#include <stdafx.h>
#include <iostream>
using namespace std;

int main()
{
	double pi = atan(1) * 4;
	int angleType;
	cout << "Degrees (1) or radians (2)?\n";
	cin >> angleType;
	double orig;
	cout << "What is the angle measure? (decimal)\n";
	cin >> orig;
	if (angleType == 1)
	{
		orig = orig * pi / 180;
		cout << "sin = " << sin(orig) << endl;
		cout << "cos = " << cos(orig) << endl;
		cout << "tan = " << tan(orig) << endl;
		cout << "csc = " << 1 / sin(orig) << endl;
		cout << "sec = " << 1 / cos(orig) << endl;
		cout << "cot = " << 1 / tan(orig) << endl;
	}
	else
	{
		bool radType;
		cout << "Is it in terms of pi? (Y=1)\n";
		cin >> radType;
		if (radType == true)
		{
			orig = pi * orig;
			cout << "sin = " << sin(orig) << endl;
			cout << "cos = " << cos(orig) << endl;
			cout << "tan = " << tan(orig) << endl;
			cout << "csc = " << 1 / sin(orig) << endl;
			cout << "sec = " << 1 / cos(orig) << endl;
			cout << "cot = " << 1 / tan(orig) << endl;
		}
		else
		{
			cout << "sin = " << sin(orig) << endl;
			cout << "cos = " << cos(orig) << endl;
			cout << "tan = " << tan(orig) << endl;
			cout << "csc = " << 1 / sin(orig) << endl;
			cout << "sec = " << 1 / cos(orig) << endl;
			cout << "cot = " << 1 / tan(orig) << endl;
		}
	}
	return 0;
}