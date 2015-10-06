// Base Converter.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	cout << "What is the number?\n";
	long firstNumber;
	cin >> firstNumber;
	cout << "What is the current base? (Between 2 and 10)\n";
	int firstBase;
	cin >> firstBase;
	cout << "What is the desired base? (Between 2 and 10)\n";
	int secondBase;
	cin >> secondBase;
	if (firstBase < 2)
	{
		cout << "\nPlease stop wasting my time.\n";
	}
	else
	{
		long Counter;
		long Digit = 0;
		long DigitTotal;
		long trueValue;
		long trueValueTotal = 0;
		long digitValue = 1;
		long digitPower;
		while (firstNumber > 0)
		{
			Counter = firstNumber;
			trueValue = 1;
			// Figuring out the first digit and its position.
			while (Counter >= 10)
			{
				Counter /= 10;
				Digit++;
			}
			DigitTotal = Digit;
			digitPower = 1;
			// Figuring out how many zeroes are behind it, for later. This is when ^ comes in handy in the real world.
			while (DigitTotal > 0)
			{
				digitPower *= 10;
				DigitTotal--;
			}
			// Figuring out how much that digit position is "worth."
			digitValue = 1;
			while (Digit > 0)
			{
				digitValue *= firstBase;
				Digit--;
			}
			// Obtaining the true value of the digit and subtracting it from the original, in order to repeat again.
			trueValue *= Counter * digitValue;
			firstNumber -= Counter * digitPower;
			trueValueTotal += trueValue;
			// Code used for debugging issues with the variables.
			// cout << endl << "digitValue = "<< digitValue;
			// cout << endl << "trueValue = " << trueValue;
			// cout << endl << "trueValueTotal = " << trueValueTotal;
			// cout << endl << "firstNumber = " << firstNumber;
			// cout << endl;
		}
		// 1011 in base 2 is 11 in base 10 and 21 in base 5.
		long trueValueTotalNew = 1;
		long secondNumber;
		long finalSolution = 0;
		while (trueValueTotalNew > 0)
		{
			long secondBasePower = 1;
			Digit = 0;
			// Finding the correct digit with a high enough value to encapsulate the number.
			while (secondBasePower <= trueValueTotal)
			{
				secondBasePower *= secondBase;
				Digit++;
				// cout << endl << "Digit = " << Digit;
				// cout << endl << "secondBasePower = " << secondBasePower;
			}
			secondBasePower /= secondBase;
			// Finding the remainder.
			trueValueTotalNew = trueValueTotal % secondBasePower;
			digitPower = 1;
			// Figuring out how many zeroes are behind it, for later. This is when ^ comes in handy in the real world.
			while (Digit > 1)
			{
				digitPower *= 10;
				Digit--;
			}
			// cout << endl << "digitPower = " << digitPower;
			secondNumber = (trueValueTotal - trueValueTotalNew) * digitPower / secondBasePower;
			trueValueTotal = trueValueTotalNew;
			finalSolution += secondNumber;
			// cout << endl << "trueValueTotal = " << trueValueTotal;
			// cout << endl << "trueValueTotalNew = " << trueValueTotalNew;
			// cout << endl << "secondNumber = " << secondNumber;
			// cout << endl << "finalSolution = " << finalSolution;
		}
		cout << endl << "Your desired number is " << finalSolution << "." << endl;
	}
}

/*
OOOOOO         CCCCCC    M MMM  MMMM   R RRRRRRR
O     OO     CC          MM    M    M  RR       R
O      O    C            M     M    M  R
O      O    C            M     M    M  R
O     OO    C            M     M    M  R
OOOOOO        CCCCCCCC   M     M    M  R
O
O
O
*/