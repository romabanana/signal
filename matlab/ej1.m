
fm = 500; # Frecuencia de muestreo
tm = 1/fm;
ti = -1; # Ti
tf = 1; # Tf
#ti:tm:tf-tm; # Hasta tf-tm para obtener n muestras de acuerdo a la frecuencia

fs = 2; # Frecuencia de la senoidal [fs e R].
phi = 0; # Fase de la senoidal [phi e (-pi, pi)]


[t, y] = gen_cuad(ti ,tf ,fm ,fs ,phi);
figure(1);
hold on;
#plot(t,y);

comet(t,y);
#comet
#stem(t,y);
#hold on;
#for fs = 1:0.2:10
 # y = senoidal(fs, t, phi);
  #stem(t,y);
  #pause(0.15);  % seconds to wait

#end
