clear all;

# 0.01s -> 8 muestras
# 1.0 s -> 800 muestras
# Tm = 1/800 -> t1 (retardo) = 5/800 = 6.25e-3
# fs = 20 hz
# phi = -0.25pi


A = 3;
fs = 20;
fm = 800; # Frecuencia de muestreo
ti = 0; # Ti
tf = 1; # Tf
phi = - pi/4; # F


#graficar con fs = 5Hz en 1s

[t, y] = gen_sen(ti, tf, fm, fs, phi);
y = A*y; # amplited

stem(t,y);
axis([0 0.1 -3 3]);
grid on;
