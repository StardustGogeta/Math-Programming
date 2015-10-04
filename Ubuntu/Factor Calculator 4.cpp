#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
    cout << "What is your number?\n";
    long inputNumber;
    cin >> inputNumber;
    if (inputNumber > 0)
	{
		for (long Divisor = 1; Divisor < sqrt(inputNumber); Divisor++)
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
