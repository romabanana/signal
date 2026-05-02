#Sist
# parte ii
a = [1 -0.6]
b = [1 0.2]
d = [1 0]

a = [a, zeros(1, 18)];
b = [b, zeros(1, 18)];
d = [d, zeros(1, 18)];

S = filter(b, a, d);

stem(0:19, S);
grid on;

# parte iii
x = (0:9)*0.1; #entrada

# a
y1 = convo(S, x);

# b
##y2 = zeros(1, length(S) + length(x) - 1);
##y2(1) = S(1) * x(1);
##y2(2) = S(1) * x(2) + S(2) * x(1);
##y2(3) = S(1) * x(3) + S(2) * x(2) + S(3) * x(1);
# Primeros 4 Valores
b = x(1:4)';
d1 = [S(1) S(1) S(1) S(1)];
d2 = [S(2) S(2) S(2)];
d3 = [S(3) S(3)];
d4 = [S(4)];

A = diag(d1) + diag(d2, -1) + diag(d3, -2) + diag(d4, -3);
y2 = (A*b)';

# c
L = length(S) + length(x) - 1;
y3 = convocir(S, x, L);

y1
y2
y3

# d


