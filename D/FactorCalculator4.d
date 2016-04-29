import std.stdio, std.math, std.container, std.conv;
void main()
{
    writeln("Enter a number.");
    long n = 0;
    stdin.readf("%d\n",&n);
    writeln();
    for (long d =1;d<=floor(sqrt(real(n)));d++)
        if (n%d == 0)
            writeln(n/d,", ",d);
    writeln("List complete!");
}
