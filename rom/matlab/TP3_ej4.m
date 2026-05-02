# Constantes
ti   = 0;
tf   = 1;
fm   = 100;
fs   = 1;
fase = 0;

# Vector de Coeficientes
coef = [1 0 0 0 0 0 0 0 0 0];

##coef = [1 4 2 0 1 0 1 2 0 0];

# 1) CL de senoidales de distinta frecuencia
[t, ycl] = gen_cl_sen10(ti, tf, fm, coef, fase);

##figure(1);
##plot(t,ycl);

parecido = zeros(1, 10);

for i = 1:10
  [_, seno]    = gen_sen(ti, tf, fm, i, fase);
  parecido(i) = dot(ycl, seno);
endfor
figure(2);
bar(parecido)

# 2) CL de senoidales de distinta fase
[t, ycl] = gen_cl_sen10_alt(ti, tf, fm, fs, coef);

##figure(3);
##plot(t,ycl);


parecido = zeros(1, 10);
fases = linspace(0, 2*pi, 10);
for i = 1:10
  [_, seno]    = gen_sen(ti, tf, fm, fs, fases(i));
  parecido(i) = dot(ycl, seno);
endfor

figure(4);
bar(parecido)

#3) Señal cuadrada de 5.5hz

[_, c5hz] = gen_cuad(ti, tf, fm, 5.5, 0);


parecido_fre = zeros(1, 10);
parecido_pha = zeros(1, 10);
fases = linspace(0, 2*pi, 10);

for i = 1:10
  # Frecuencia
  [_, seno_2]     = gen_sen(ti, tf, fm, i, fase);
  parecido_fre(i) = dot(c5hz, seno);

  # Phsae
  [_, seno_2]     = gen_sen(ti, tf, fm, fs, fases(i));
  parecido_pha(i) = dot(c5hz, seno);
endfor

figure(5);
bar(parecido_fre);
figure(6);
bar(parecido_pha);

