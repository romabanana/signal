# Constantes
ti = 0;
tf = 1;
fm = 100;

# Senoidal 1
A_1    = 1;
fs_1   = 10;
fase_1 = 0;

[t, senoidal_1]  = gen_sen(ti, tf, fm, fs_1, fase_1);
senoidal_1       = senoidal_1 * A_1;



frecuencias = [0.5 1 2 3 5 10 20 30 40 50];
n          = length(frecuencias);
productos  = zeros(1, n);

# Senoidal 2
A_2    = 1;
##fs_2   = 10;
fase_2 = 0;


for i = 1:n
  [t, senoidal_2]  = gen_sen(ti, tf, fm, frecuencias(i), fase_2);
  senoidal_2       =  senoidal_2 * A_2;

  productos(i)     = dot(senoidal_1, senoidal_2);
endfor

stem(frecuencias, productos);


