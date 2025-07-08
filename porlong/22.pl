bird(sparrow).
bird(penguin).
bird(eagle).
bird(ostrich).
bird(parrot).
cannot_fly(penguin).
cannot_fly(ostrich).
can_fly(Bird) :-
    bird(Bird),
    \+ cannot_fly(Bird).
