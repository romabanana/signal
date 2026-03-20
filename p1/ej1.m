
fm = 20; # Frecuencia de muestreo
tm = 1/fm;
ti = -1; # Ti
tf = 1; # Tf
#ti:tm:tf-tm; # Hasta tf-tm para obtener n muestras de acuerdo a la frecuencia

fs = 1; # Frecuencia de la senoidal [fs e R].
phi = 0; # Fase de la senoidal [phi e (-pi, pi)]


[x, y] = gen_sinc(ti ,tf ,fm ,fs ,phi);
figure(1);
hold on;
#plot(t,y);

stem(x,y);
#comet
#stem(t,y);
#hold on;
#for fs = 1:0.2:10
 # y = senoidal(fs, t, phi);
  #stem(t,y);
  #pause(0.15);  % seconds to wait
  
#end
