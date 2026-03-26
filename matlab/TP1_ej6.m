clear all;
fs = 1;
fm = 10; # Frecuencia de muestreo
ti = 0; # Ti
tf = 1; # Tf
phi = 0; # F


#graficar con fs = 5Hz en 1s

[t, y] = gen_sen(ti, tf, fm, fs, phi);
grid on;
hold on;
axis([0 2 -1 1]);
title(["Interpolador" num2str(fm) "Hz"]);
[t4, interpolada] = sobremuestrear(y, ti, tf, fm, 4, @sinc_aux3);
size(interpolada)
size(t4)
stem(t4,interpolada);


