#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include "Eigen/Dense"
using namespace std;
using Eigen::MatrixXd;

int main()
{
	cout << "Enter your three coordinate points, separated by spaces.\n";
	double a,b,c,d,e,f,D,E,F;
	cin >> a>>b>>c>>d>>e>>f;
	MatrixXd m(3,1), m2(3,3);
	m << -(pow(a,2)+pow(b,2)),-(pow(c,2)+pow(d,2)),-(pow(e,2)+pow(f,2));
	m2 << a,b,1,c,d,1,e,f,1;
	MatrixXd DEF(3,1);
	DEF << m2.inverse() * m;
	D=DEF(0)/-2,E=DEF(1)/-2,F=DEF(2);
	char A = 253;
	cout << setprecision(3) << "(x - "<<D<<")"<<A<<" + (y - "<<E<<")"<<A<<" = "<<-F+pow(D,2)+pow(E,2);
}
