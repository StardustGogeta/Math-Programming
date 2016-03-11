#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main()
{
	cout << "What is the number?\n";				string fN;	cin >> fN;
	cout << "What is the current base? (<=36)\n";	int fB;		cin >> fB;
	cout << "What is the desired base? (<=10)\n";	int sB;		cin >> sB;
	if (1<fB<37 && 1<sB<11)
	{
		long tVT = stoi(fN, nullptr, fB);
		string sN;
		while (tVT)
		{
			sN += to_string(tVT%sB);
			tVT = floor(tVT / sB);
		}
		cout << "\nYour number is ";
		for (string::reverse_iterator rit = sN.rbegin(); rit != sN.rend(); ++rit)
			cout << *rit;
		cout << ".\n";
	}
	else
	{
		cout << "\nStop wasting time.\n";
	}
}
