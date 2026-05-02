# Constantes
ti = 0;
tf = 1;
fm = 100;

# Senoidal 1
A_1    = 1;
fs_1   = 10;
fase_1 = 0;

[t, senoidal_1]  = gen_sen(ti, tf, fm, fs_1, fase_1);
senoidal_1 = senoidal_1 * A_1;

# Senoidal 2
A_2    = 1;
fs_2   = 10;
fase_2 = 0;

[t, senoidal_2]  = gen_sen(ti, tf, fm, fs_2, fase_2);
senoidal_2 =  senoidal_2 * A_2;

dot(senoidal_1, senoidal_2)
