
fs = 5;
fm = 100; # Frecuencia de muestreo
tm = 1/fm;
ti = 0; # Ti
tf = 1; # Tf
phi = 0; # F


#Rectificion

[t, y] = gen_sen(ti, tf, fm, fs, phi);

y_modificada = rectificar(y);

subplot(2,1,1);
grid on;
hold on;
axis([0 1 -1 1]);
title("Señal Original");
stem(t,y);
subplot(2,1,2);
hold on;
grid on;
axis([0 1 -1 1]);
title("Señal Modificada");
stem(t,y_modificada);

