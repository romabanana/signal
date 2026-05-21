#1
fs_1       = 10;
fs_2       = 20;
fs_3       = 11;
fs_4       = 10.5;
tini       = 0;
tfin       = 1;
tfin_2     = 2;
fm         = 1000; #T = 0.001 s
fase       = 0.0;

[t, sin_1] = gen_sen(tini, tfin, fm , fs_1, fase);
[_, sin_2] = gen_sen(tini, tfin, fm , fs_2, fase);
[_, sin_3] = gen_sen(tini, tfin, fm , fs_3, fase);
[_, sin_4] = gen_sen(tini, tfin, fm , fs_4, fase);
[d, sin_5] = gen_sen(tini, tfin_2, fm , fs_1, fase);
[_, sin_6] = gen_sen(tini, tfin_2, fm , fs_4, fase);


s_t        = sin_1 + (4 * sin_2);
S_t        = abs(fft(s_t));

##stemft(S_t, t, fm);

#2 Verificar Parseval
N    = length(s_t);

Es_1 = sum(s_t.^2);
Es_2 = (1/N) * sum(S_t.^2);
# iguales

#3
#a

s_3a = s_t + 4;
S_3a = abs(fft(s_3a));
##stemft(S_3a, t, fm);

# pico en 0hz ya que exp(0) = 1 entonces S_t(0) = sum(s_t),
# notar la senoidal se cancela a si misma y prevalece el offset..

#b
s_3b = sin_1 + 4*sin_3;
S_3b = abs(fft(s_3b));
##stemft(S_3b, t, fm);

# nada raro

#c
s_3c = sin_1 + 4*sin_4;
##S_3c = abs(fft(s_3c));

##stemft(S_3c, t, fm);
# la sin de 10.5 hz completa 10.5 ciclos en 1s y produce el fenemeno el la ft
#d
s_3d = sin_5 + 4*sin_6;
S_3d = abs(fft(s_3d));

##stemft(S_3d, d, fm);
# si tfin = 2s entonce la sin completa 21 ciclos y le df es 0.5 hz, y por ende
# se representa correctamente..
