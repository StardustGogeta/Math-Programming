// Factor Calculator 4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int main()
{
	cout << "What is your number?\n";
	__int64 n;
	cin >> n;
	if (n)
	{
		for (__int64 Divisor = 1; Divisor < sqrt(n); Divisor++)
		{
			if (n % Divisor == 0)
			{
				cout << n / Divisor << "\n" << Divisor << "\n";
			}
		}
		cout << "\nThe list of factors has been successfully generated.\n";
	}
	else
	{
		cout << "Sorry, I can't do that.\n";
	}
}