import std.stdio, std.random, std.conv;
void main()
{
	double t,h,f,c=0,x=0,y,r;
	writeln("How many heads, flips, and trials? (Separate with spaces)");
	stdin.readf("%g %g %g\n",&h,&f,&t);
	for (;x<t;x++) {
		r=0;
		for (y=0;y<f;y++) {
			r += uniform01()>=.5;
		}
		c += r==h;
	}
	writefln("This combination will happen %.4g%% of the time.",c*100/t);
}
