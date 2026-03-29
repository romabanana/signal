clear all;
fs = 5;
frecuencias = [100 25 10 4 1 0.5]; # Frecuencia de muestreo
ti = 0; # Ti
tf = 1; # Tf
phi = 0; # F


#graficar con fs = 5Hz en 1s
#fm, 100, 25, 4, 1,  0.5

[_, size] = size(frecuencias)
index = 1;
for fm = frecuencias
  [t, y] = gen_sen(ti, tf, fm, fs, phi);
  subplot(size,1,index);
  grid on;
  hold on;
  axis([0 1 -1 1]);
  title(["Frecuencia de muestro " num2str(fm) "Hz"]);
  stem(t,y);
  index += 1;
endfor

