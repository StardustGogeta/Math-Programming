coterminal(THETA, RET) :-
    THETA >= 0,
    THETA < 2*pi,
    RET is THETA.

coterminal(THETA, RET) :-
    THETA < 0,
    RET is THETA + 2*pi*ceil(-THETA/2/pi).

coterminal(THETA, RET) :-
    THETA >= 2*pi,
    RET is THETA - 2*pi*floor(THETA/2/pi).

