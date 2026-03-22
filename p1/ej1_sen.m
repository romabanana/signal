#Ejerciciio uni def...

fm = 100; # Frecuencia de muestreo
tm = 1/fm;
ti = 0; # Ti
tf = 1; # Tf
phi = 0; # F


# Frecuencia de la senoidal [fs e R].

figure(1);

[t, y] = gen_sen(ti, tf, fm, 1, phi);

h1 = plot(t, y);     % line
hold on;
h2 = stem(t, y);     % discrete points

grid on;
axis([0 1 -1 1]);

for fs = 1:1:50
  [t, y] = gen_sen(ti, tf, fm, fs, phi);

  set(h1, "ydata", y);
  set(h2, "ydata", y);

  title(sprintf("Senoidal de frecuencia: %d Hz muestreada a 100hz", fs));
  pause(0.3)
  drawnow;
endfor
