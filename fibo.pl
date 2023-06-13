fibonacci(0, [0]).
fibonacci(1, [0, 1]).
fibonacci(N, Sequence) :-
    N > 1,
    fibonacci(N, [0, 1], Sequence).

fibonacci(N, [A, B | Rest], Sequence) :-
    N > 1,
    Sum is A + B,
    fibonacci(N, [Sum, A, B | Rest], Sequence).
fibonacci(N, Sequence, Sequence) :-
    length(Sequence, Length),
    Length =:= N + 1.


?- fibonacci(0, Sequence).
Sequence = [0].

?- fibonacci(1, Sequence).
Sequence = [0, 1].

?- fibonacci(10, Sequence).
Sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55].
