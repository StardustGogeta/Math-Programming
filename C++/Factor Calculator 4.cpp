#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	cout << "What is your number?\n";
	__int64 n;
	cin >> n;
	if (n>0)
	{
		for (__int64 d=1; d<=sqrt(n); d++)
			if (!(n%d))
				cout << n/d << ", " << d << "\n";
		cout << "\nThe list of factors has been successfully generated.\n";
	}
	else
		cout << "Sorry, I can't do that.\n";
}
