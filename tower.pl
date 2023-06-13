hanoi(N) :-
    hanoi(N, left, middle, right).

hanoi(1, Source, _, Destination) :-
    write('Move top disk from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl.

hanoi(N, Source, Auxiliary, Destination) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Destination, Auxiliary),
    hanoi(1, Source, _, Destination),
    hanoi(M, Auxiliary, Source, Destination).


?- hanoi(3).
Move top disk from left to right
Move top disk from left to middle
Move top disk from right to middle
Move top disk from left to right
Move top disk from middle to left
Move top disk from middle to right
Move top disk from left to right
true.
