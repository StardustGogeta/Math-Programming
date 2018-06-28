factor(X, D) :- % If D divides X, it is a factor.
	0 is X mod D.

factorCheck(X, 1, Factors, Final) :-
	Final = [1|[X|Factors]].
	
factorCheck(X, N, Factors, Final) :-
	factor(X, N),
	D is X/N,
	N2 is N-1,
	factorCheck(X, N2, [N|[D|Factors]], Final).
	
factorCheck(X, N, Factors, Final) :-
	N2 is N-1,
	factorCheck(X, N2, Factors, Final).

fc4(X, Factors) :- % Returns a list of factors of X
	N is floor(sqrt(X)),
	factorCheck(X, N, [], Factors). 
