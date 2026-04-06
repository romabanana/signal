clear all;
ti = 0;
tf = 1;
fm = 200;
fs = 60;

#
#
#
#

[t, ruido] = gen_aleatoria(ti, tf, fm, 1);
[_, senal1] = gen_sen(ti, tf, fm, 2*fs, 0);
[_, senal2] = gen_sen(ti, tf, fm, fs, pi*0.4);
[_, senal3] = gen_sen(ti, tf, fm, 4*fs, pi*0.2);

senal = senal1 + senal2 + senal3;

potencia_senal = potencia(senal)
potencia_ruido = potencia(ruido)
senal_con_ruido = ruido' + senal;
plot(t, senal)
hold on,
plot (t, ruido)
relacion_senal_ruido = potencia_senal/potencia_ruido


ruido_por_2 = 2*ruido;                      # r = ar0
potencia_ruido_2 = potencia(ruido_por_2)
potencia_ruido_2 = potencia_ruido * 4   % 2²    # Pr = a²Pr0

relacion_sena_ruido_2= potencia_senal/potencia_ruido


beta = potencia_senal/potencia_ruido;
potencia_0_db = beta * potencia_ruido;
relacion_sena_ruido_0db = potencia_senal/potencia_0_db

