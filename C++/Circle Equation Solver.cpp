#include <iostream>
#include <iomanip>
#include "Eigen/Dense"
using namespace std;
using Eigen::MatrixXd;

int main()
{
	cout << "Enter your three coordinate points, separated by spaces.\n";
	double a,b,c,d,e,f,D,E,F;
	cin >> a>>b>>c>>d>>e>>f;
	MatrixXd m(3,1), m2(3,3);
	m << -a*a-b*b,-c*c-d*d,-e*e-f*f;
	m2 << a,b,1,c,d,1,e,f,1;
	MatrixXd DEF(3,1);
	DEF << m2.inverse()*m;
	D=DEF(0)/-2,E=DEF(1)/-2,F=DEF(2);
	char A=253;
	cout <<setprecision(3)<<"(x - "<<D<<")"<<A<<" + (y - "<<E<<")"<<A<<" = "<<-F+D*D+E*E;
}
