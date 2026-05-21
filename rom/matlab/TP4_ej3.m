#3 Verifique propiedad de retardo temporal de la tdf
fs_1       = 10;
tini       = 0;
tfin       = 1;
fm         = 100;
fase       = 0.0;

[t, s_a] = gen_sen(tini, tfin, fm , fs_1, fase);
S_a      = fft(s_a);

m = 1;
N = length(t);
k = 0:N-1;
e = exp(-j * (2*pi/N) * k * m);

S_b = S_a .* e;

s_b = real(ifft(S_b));

figure(1);
stem(t, s_a);
figure(2);
stem(t, s_b);

