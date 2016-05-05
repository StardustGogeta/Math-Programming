#include <cmath>
#include <iostream>
using namespace std;

int main()
{
	cout <<"State an angle.\n";
	__int64 o;
	cin >> o;
	o=o%360;
	cout <<"Coterminal angles include "<<o<<" and " <<o-copysignl(360,o)<<".\n";
}
