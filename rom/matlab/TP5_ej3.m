clear;
clc;
pkg load signal;
hold on;
fm = 10000; %(10 kHz)
N = 150; # numero de puntos
w = linspace(0, 2*pi, N); #circulo
z = exp(1i * w); #si r = 1 -> Z es equivalente a TFTD
frecuencias = (w / (2*pi)) * fm;

%1

H     = @(z)...
        (1 - 2 .* (z .^ -1) + 2 .* (z .^ -2) - (z .^ -3))...
        ./...
        ((1 - z .^ -1) .* (1 - 0.5 .* (z .^ -1)) .* (1 - 0.2 * (z .^ -1)));

b = [1, -2, 2, -1];
##(1−z−1)=0⟹z=1
##
##(1−0.5z−1)=0⟹z=0.5
##
##(1−0.2z−1)=0⟹z=0.2
a = [1, -1.7, 0.8, -0.1];
polos = roots(a)
ceros = roots(b)


H_f = H(z);
figure(1);
stemft_half(abs(H_f), frecuencias, fm);
figure(2);
zplane(b, a);
title('Z-Plane');
set(findobj(gca, 'Type', 'line'), 'LineWidth', 2);
grid on;
