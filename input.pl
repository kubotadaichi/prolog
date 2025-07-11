parent(john, mary).
parent(john, anne).
parent(mary, alice).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).