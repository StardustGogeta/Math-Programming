// Factor Calculator 4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int main()
{
	cout << "What is your number?\n";
	__int64 inputNumber;
	cin >> inputNumber;
	// Asking for the original number and checking that it is a legal one.
	if (inputNumber > 0)
	{
		for (__int64 Divisor = 1; Divisor < sqrt(inputNumber); Divisor++)
		/* You might be wondering, why square root?
		It is the perfect solution to the problem because
		all factors will be either under the square root or multiply with one below it,
		so there is no use in brute-forcing it. It will check every integer divisor up until
		that point, including the counterparts along the way. It can only calculate the factors
		of 64-bit numbers, so you cannot mash numbers and expect to get an answer. */
		{
			if (inputNumber % Divisor == 0)
			{
				cout << inputNumber / Divisor << "\n" << Divisor << "\n";
			}
		}
		cout << endl << endl << "The list of factors has been successfully generated.\n";
	}
	else
	{
		cout << "Are you trying to kill me?\n" << "You will pay for that.\n";
	}
    return 0;
}

