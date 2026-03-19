
fm = 29; # Frecuencia de muestreo.
tm = 1/fm;
ti = 0; # Ti
tf = 2; # Tf
t = ti:tm:tf-tm; # Hasta tf-tm para obtener n muestras de acuerdo a la frecuencia

fs = 1; # Frecuencia de la senoidal [fs e R].
phi = 0; # Fase de la senoidal [phi e (-pi, pi)]


#comet
#stem(t,y);
for phi = 0:0.2:pi/2
  y = senoidal(fs, t, phi);
  stem(t,y)
  pause(0.25);  % seconds to wait
end
