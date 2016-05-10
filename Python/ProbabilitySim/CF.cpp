#include <iostream>
#include <cstdlib>
using namespace std;
int main(int argc, char *argv[])
{
	double h=stod(argv[1]),f=stod(argv[2]),t=stod(argv[3]),s=0,r,x=0,y;
	for(x;x<t;x++)
	{
		r = 0;
		for(y=0;y<f;y++)
			r += rand()%2?1:0;
		s += r==h?1:0;
	}
	return s/t*100;
}
