# Constantes
ti = 0;
tf = 1;
fm = 100;

# Senoidal 1
A_1    = 1;
fs_1   = 1;
fase_1 = 0;

[t, senoidal_1]  = gen_sen(ti, tf, fm, fs_1, fase_1);
[t, senoidal_2]  = gen_sen(ti, tf, fm, fs_1, fase_1+pi);

hold on;
plot(t, senoidal_1);
plot(t, senoidal_2);
