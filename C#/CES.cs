using System;
using System.Collections.Generic;
using System.Linq;
using MathNet.Numerics.LinearAlgebra;
using MathNet.Numerics.LinearAlgebra.Double;

namespace CES
{
    class Program
    {
        static void Main(string[] args)
        {
            // -2 7 -9 0 -10 -5
            Console.WriteLine("Enter your three coordinate points, separated by spaces.");
            string[] input = Console.ReadLine().Split(' ');
            List<double> r=input.Select(x=>double.Parse(x)).ToList();
            double a=r[0],b=r[1],c=r[2],d=r[3],e=r[4],f=r[5],D,E,F;
            Matrix<double> m = DenseMatrix.OfArray(new double[,] {{-a*a-b*b},{-c*c-d*d},{-e*e-f*f}});
            Matrix<double> m2 = DenseMatrix.OfArray(new double[,]{{a,b,1},{c,d,1},{e,f,1}});
            Matrix<double> DEF = m2.Solve(m);
            D = DEF[0,0]/-2;
            E = DEF[1,0]/-2;
            F = DEF[2,0];
            Console.WriteLine("(x - "+D+")\u00b2 + (y - "+E+")\u00b2 = "+(-F+D*D+E*E).ToString());
        }
    }
}