clear all;
ti = 0;
tf = 1;
fm = 200;
fs = 60;


[t, ruido] = gen_aleatoria(ti, tf, fm, 1);
[t, senal] = gen_sen(ti, tf, fm, fs, 0);

potencia_senal = potencia(senal)
potencia_ruido = potencia(ruido)
senal_con_ruido = ruido' + senal;
#plot(t,senal_con_ruido)
relacion_sena_ruido = potencia_senal/potencia_ruido


ruido = 2*ruido;
potencia_ruido = potencia(ruido)
relacion_sena_ruido_2= potencia_senal/potencia_ruido

