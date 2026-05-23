y  = load('necg.txt'); #samples 1024
y  = y';
fm = 360;
ti = 0;
tf = length(y)/fm;
T  = 1/fm;
t  = ti:T:tf - T;
Y  = fft(y);

##stemft(abs(Y), t, fm);
N  = length(y);
df = fm/N;
k  = (0:N-1) * df;

H  = ones(1, N);
H(k > 40) = 0;
H(k > (fm - 40)) = 1;
##plot(k,H);3

S_filter = H .* Y;

y_filtered = real(ifft(S_filter));

figure(1);
stem(t, y);
figure(2);
stem(t, y_filtered);
