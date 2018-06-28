% Write repCount(L, X, N) which is true when N is the number of occurrences of X in list L

match(X, X, N, N+1). % If first two arguments are equal, return N+1
	
match(_, _, N, N). % Otherwise, return N

checkReps([], _, N, N). % If checking empty list, return number of matched characters
	
checkReps(L, X, N, M) :- % Otherwise,
	[H|T] = L,
	match(H, X, N, N2), % Check the first character for a match
	checkReps(T, X, N2, M). % and check the rest of the list

repCount(L, X, M) :- % Make a wrapper for the function
	checkReps(L, X, 0, N),
	M is N.
	
% repCount([1,1,1,2,2,3,5,5,4],1,X).