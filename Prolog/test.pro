test(X,Y) :-
    var(Y),
    Y is 3 * X.

test(X,Y) :-
    Y < 0,
    X is 2 * Y.

test(X,Y) :-
    X is Y.

sum(X,Y,Z) :-
    nonvar(Z),
    nonvar(X),
    nonvar(Y),
    Z is X + Y.

sum(X,Y,Z) :-
    var(Z),
    nonvar(X),
    nonvar(Y),
    Z is X + Y.

sum(X,Y,Z) :-
    var(X),
    nonvar(Z),
    nonvar(Y),
    X is Z - Y.

sum(X,Y,Z) :-
    var(Y),
    nonvar(Z),
    nonvar(X),
    Y is Z - X.

move(1,X,Y,_) :-
    write('Move top disk from '),
    write(X),
    write(' to '),
    write(Y),
    nl.
move(N,X,Y,Z) :-
    N>1,
    M is N-1,
    move(M,X,Z,Y),
    move(1,X,Y,_),
    move(M,Z,Y,X).
