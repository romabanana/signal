y  = load('necg.txt'); #samples 1024
y  = y';
fm = 360;
ti = 0;
tf = length(y)/fm;
T  = 1/fm;
t  = ti:T:tf - T;
Y  = fft(y);


##stemft(abs(Y), t, fm);
