clear all;
fs = 4000;
fm = 129; # Frecuencia de muestreo
ti = 0; # Ti
tf = 2; # Tf
phi = 0; # F


#graficar con fs = 5Hz en 1s

[t, y] = gen_sen(ti, tf, fm, fs, phi);
grid on;
hold on;
axis([0 2 -1 1]);
title(["Señal de 4000Hz con Frecuencia de muestro " num2str(fm) "Hz"]);
stem(t,y);


