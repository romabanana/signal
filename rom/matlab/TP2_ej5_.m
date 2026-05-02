A = [2 1 0.5]
B = [1 2 2]

R = [2 5 6.5 3 1]
h = convo(A,B)

#filter

A_pad = [A zeros(1, length(B) - 1)];

# 1

F = filter(B, 1, A_pad)
