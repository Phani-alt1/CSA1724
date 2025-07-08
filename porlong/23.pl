male(john).
male(paul).
male(mike).
female(lisa).
female(susan).
female(anna).

parent(john, paul).
parent(john, susan).
parent(lisa, paul).
parent(lisa, susan).
parent(paul, mike).
parent(anna, mike).

father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
