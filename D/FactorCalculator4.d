import std.stdio, std.math, std.container, std.conv;
void main()
{
    char[] buf;
    writefln("Hello!");
    auto n = to!long(stdin.readln(buf));
    /*writefln(n);
    /*if (n > 0)
    {
        long[] numbers = [1,n];
        for (long d=1;d<=std.math.sqrt(n)+1;d++)
        {
            if (n % d == 0)
            {
                std.container.dlist.insertBack(numbers)([int(n/d),d]);
            }
        }
        numbers.sort();
        return(numbers);
    }
    else
    {
        return("Error!");
    }*/
}
