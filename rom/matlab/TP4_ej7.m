# Part I #
A1 = 5;
A2 = 3;
A3 = 2;

f1 = 50;
f2 = 120;
f3 = 280;

ti = 0;
tf = 1;
fm = 1000;

fase = 0

[t, aux_sen_1] = gen_sen(ti, tf, fm, f1, fase);
[_, aux_sen_2] = gen_sen(ti, tf, fm, f2, fase);
[_, aux_sen_3] = gen_sen(ti, tf, fm, f3, fase);

s_n = A1 * aux_sen_1 + A2 * aux_sen_2 + A3 * aux_sen_3;

S_n = fft(s_n);
figure(1);
stemft(abs(S_n), t, fm);
##N       = length(s_n);
##delta_f = fm/ N
##
### con fm = 200;
##fm = 200
##[t, aux_sen_1] = gen_sen(ti, tf, fm, f1, fase);
##[_, aux_sen_2] = gen_sen(ti, tf, fm, f2, fase);
##[_, aux_sen_3] = gen_sen(ti, tf, fm, f3, fase);
##
##s_n = A1 * aux_sen_1 + A2 * aux_sen_2 + A3 * aux_sen_3;
##
##S_n = fft(s_n);
##figure(2);
##stemft(abs(S_n), t, fm);

#f1 = 50; -> cumple < fm/2 = 100hz
#f2 = 120;-> no cumple
# f_a = abs(120-200) = 80hz
#f3 = 280;
# f_a = abs(280-200) = 80hz

#picos

# Part II #

##A1 = 5;
##A2 = 3;
##A3 = 2;
##
##f1 = 50;
##f2 = 120;
##f3 = 280;
##
##ti = 0;
####tf = 1;
##tf = 0.004;
##fm = 1000;
##
##fase = 0
##
##[t, aux_sen_1] = gen_sen(ti, tf, fm, f1, fase);
##[_, aux_sen_2] = gen_sen(ti, tf, fm, f2, fase);
##[_, aux_sen_3] = gen_sen(ti, tf, fm, f3, fase);
##
##s_n = A1 * aux_sen_1 + A2 * aux_sen_2 + A3 * aux_sen_3;
##
##N       = length(s_n);
##delta_f = fm/ N
##S_n = fft(s_n);
##figure(1);
##stem(1:delta_f:tf, abs(S_n));
####stemft(abs(S_n), t, fm);
###Zero padding
##pad = zeros(1, 40*N);
##s_n = [s_n pad];
##S_n = fft(s_n);
##figure(2);
##stem(1:delta_f:tf, abs(S_n));

# Part III #

##x1 = A1 * aux_sen_1;
##x2 = A2 * aux_sen_2;
##x3 = A3 * aux_sen_3;
##
##S1 = fft(x1);
##S2 = fft(x2);
##S3 = fft(x3);
##
##S_suma = S1 + S2 + S3;
##figure(2);
##stemft(abs(S_suma), t, fm);
##
###2 Verificar Parseval
##N    = length(S_suma);
##
##Es_1 = sum(x1.^2) + sum(x2.^2) + sum(x3.^2);
##Es_2 = (1/N) * sum(abs(S_suma).^2);

# Part IV #

N  = length(s_n);
df = fm/N;
k  = (0:N-1) * df;

H  = ones(1, N);
H(k > 200) = 0;
H(k > (fm - 200)) = 1;
##plot(k,H);

S_filter = H .* S_n

figure(2);
stemft(abs(S_filter), t, fm);

##
s_filter = real(ifft(S_filter));
figure(3);
hold on;
stem(t, s_n);
stem(t, s_filter);



