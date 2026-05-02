n   = 5;
m_v = 0:n-1;

# defino h_a
h_a = sin(8 * m_v);

# defino h_b

a = 0.5; # |a| < 1, a e R

h_b = a .^ m_v;

# defino x[n]

x = zeros(1, 5);
x(1) = 1; # x[0] = 1
x(2) = a; # x[1] = a

# Primer sistema
# x[n] ->[ h_a ]-> w1[n] ->[ h_b ]-> y[n]

w1 = convo(x, h_a);
y1  = convo(w1, h_b)

# Segundo sistema
# x[n] ->[ h_b ]-> w2[n] ->[ h_a ]-> y[n]

w2 = convo(x, h_b);
y2  = convo(w2, h_a)

# Son conmutativos
