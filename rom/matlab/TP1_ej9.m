# Part One
A = 5;
fs = 10;
phi = 0.25*pi;
fm = 400;
ti = 0;
tf = 2;
N  = 16;


[t, y] = gen_sen(ti, tf, fm, fs, phi);
y = A*y;

y_modificada = cuantizar(rectificar(y), N, A/(N-1), @round);

plot_type = 1; % 0 -> subplot; 1 -> overlay;
plott(plot_type, t, [y; y_modificada]);

