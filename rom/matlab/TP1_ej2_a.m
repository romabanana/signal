fm = 100; # Frecuencia de muestreo
tm = 1/fm;
ti = 0; # Ti
tf = 1; # Tf
phi = 0; # F


#Inversion
fs = 1;

[t, y] = gen_sen(ti, tf, fm , fs, phi);
[p, y_inv] =  gen_sen_inversa(ti, tf, fs);

subplot(2,1,1);
plot(t,y)
subplot(2,1,2);
plot(p,y_inv)



