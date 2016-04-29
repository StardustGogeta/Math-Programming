using System;

namespace FC4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number.");
            long n = Convert.ToInt64(Console.ReadLine());
            Console.WriteLine();
            for (long x = 1; x <= Math.Floor(Math.Sqrt(n)); x++)
                if (n % x == 0)
                    Console.WriteLine(n / x + ", " + x);
            Console.WriteLine();
            Console.WriteLine("List complete.");
        }
    }
}
