
fs = 1;
fm = 500; # Frecuencia de muestreo
tm = 1/fm;
ti = 0; # Ti
tf = 1; # Tf
phi = 0; # F


#Cuantificacion

[t, y] = gen_sen(ti, tf, fm, fs, phi);

minimo = min(y);
offset = 0.2
y_modificada = y - minimo + offset;

N = 6; # Numero de niveles
H = 0.5; # Magnitud del cuanto (paso).


y_modificada = cuantizar(y_modificada, N, H, @fix); #@f: funcion para quedarse con el int

y_modificada = y_modificada + minimo - offset;


subplot(2,1,1);
grid on;
hold on;
axis([0 1 -5 5]);
title("Señal Original");
stem(t,y);
subplot(2,1,2);
hold on;
grid on;
axis([0 1 -5 5]);
title("Señal Modificada");
stem(t,y_modificada);

