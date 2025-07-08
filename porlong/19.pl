s(alice). s(bob). s(carol).
t(smith). t(jones).
sub(cs101). sub(ma202).
teach(smith, cs101). teach(jones, ma202).
enroll(alice, cs101). enroll(bob, cs101). enroll(carol, ma202).
st(S,T):-enroll(S,C),teach(T,C).
