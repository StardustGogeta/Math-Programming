#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
	double h,f,t,s=0,r,x=0,y;
	cout <<"How many heads / flips / trials? (Separate with spaces.)\n";
	cin >>h>>f>>t;
	for(x;x<t;x++)
	{
		r = 0;
		for(y=0;y<f;y++)
			r += rand()%2?1:0;
		s += r==h?1:0;
	}
	cout <<"This combination will happen "<<s/t*100<<"% of the time.";
}
