avg(X,Y,Z) :- % Return the average of two values
	Z is (X+Y)/2.

slopeMidpoint(A,B, C,D, E,F,S) :- % Return the perpendicular slope S and midpoint between two points
	avg(A,C,E),
	avg(B,D,F),
	S is (A-C)/(D-B).
	
distance(A,B, C,D, R) :- % Return the distance between two points
	R is sqrt((A-C)**2+(B-D)**2).
	
intersect(A,B, C,D, S,S2, H,K) :- % Find the intersection of two point-slope sets
	% Some algebra to isolate the variable H
	% (H-A)*S = K-B
	% (H-C)*S2 = K-D
	% S(H-A)+B=S2(H-C)+D
	% H(S-S2)-SA+B+S2*C-D = 0
	H is (D-B+S*A-S2*C) / (S-S2),
	K is (H-A) * S+B.
	
ces(X0,Y0, X1,Y1, X2,Y2, H,K,R) :- % Find the center and radius of a circle given three points
	slopeMidpoint(X0,Y0, X1,Y1, A,B,S),
	slopeMidpoint(X0,Y0, X2,Y2, C,D,S2),
	intersect(A,B, C,D, S,S2, H,K),
	distance(X0,Y0, H,K, R),
	R2 is R**2,
	format('The center is (~3f,~3f).~nThe equation of the circle is (x-~3f)\u00b2+(y-~3f)\u00b2=~3f.~n',[H,K,H,K,R2]).
	
% ces(-2,7,-9,0,-10,-5, H,K,R).
