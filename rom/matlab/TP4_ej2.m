#1
fs_1       = 2;
fs_2       = 4;
fs_3       = 3.5;
tini       = 0;
tfin       = 1;
fm         = 100;
fase       = 0.0;

[t, s_a] = gen_sen(tini, tfin, fm , fs_1, fase);
[_, s_b] = gen_cuad(tini, tfin, fm , fs_1, fase);
[_, s_c] = gen_sen(tini, tfin, fm , fs_2, fase);
[_, s_d] = gen_sen(tini, tfin, fm , fs_3, fase);

dot_ab   = dot(s_a, s_b)
dot_bc   = dot(s_b, s_c)
dot_ac   = dot(s_a, s_c)

#2

##S_a = abs(fft(s_a));
##S_b = abs(fft(s_b));
##S_c = abs(fft(s_c));
S_a = fft(s_a);
S_b = fft(s_b);
S_c = fft(s_c);
S_d = fft(s_d);

figure(1);
stemft(abs(S_a), t, fm);
figure(2);
stemft(abs(S_b), t, fm); # armonicos 6hz(1/3) 10hz(1/5) 14hz(1/7)...
figure(3);
stemft(abs(S_c), t, fm);
N = length(t);

##dot_AB   = dot(S_a, conj(S_b)) / N
##dot_BC   = dot(S_b, conj(S_c)) / N
##dot_AC   = dot(S_a, conj(S_c)) / N
dot_AB   = dot(S_a, S_b) / N
dot_BC   = dot(S_b, S_c) / N
dot_AC   = dot(S_a, S_c) / N

#3
dot35_t =  dot(s_a, s_d)
dot35_f =  dot(S_a, S_d) / N



