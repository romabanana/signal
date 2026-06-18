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

H     = @(z) 1./(1-1/2.*(z.^-1)+ 1/4.*(z.^-2));
b     = [1];
a     = [1, -0.5, 0.25];
polos = roots(a);
ceros = roots(b);

angulo_polo = angle(polos(1));
f_pico_hz   = angulo_polo * (fm / (2*pi));
radio       = abs(polos(1));

fprintf('Polo: %.2f Hz\n', f_pico_hz);
fprintf('Radio en el circulo: %.2f\n', radio);

H_f = H(z);
figure(1);
stemft_half(abs(H_f), frecuencias, fm);
line([f_pico_hz, f_pico_hz], [0, max(abs(H_f))], 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1.5);
figure(2);
zplane(b, a);
title('Z-Plane');
set(findobj(gca, 'Type', 'line'), 'LineWidth', 2);
grid on;
%2

##H = @(z) (z.^-1)./(1-(z.^-1)-(z.^-2));
##b     = [0, 1];
##a     = [1, -1, -1];
##polos = roots(a);
##ceros = [0];
##
##angulo_polo = angle(polos(1));
##f_pico_hz   = angulo_polo * (fm / (2*pi));
##radio       = abs(polos(1));
##
##fprintf('Polo: %.2f Hz\n', f_pico_hz);
##fprintf('Radio en el circulo: %.2f\n', radio);
##
##angulo_cero = angle(ceros(1));
##f_valle_hz  = angulo_cero* (fm / (2*pi));
##radio       = abs(ceros(1));
##
##fprintf('Cero: %.2f Hz\n', f_valle_hz);
##fprintf('Radio en el circulo: %.2f\n', radio);
##
##H_f = H(z);
##stemft_half(abs(H_f), frecuencias, fm);
##line([f_pico_hz, f_pico_hz], [0, max(abs(H_f))], 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1.5);
##line([f_valle_hz, f_valle_hz], [0, max(abs(H_f))], 'Color', 'b', 'LineStyle', '--', 'LineWidth', 1.5);
##figure(2);
##zplane(b, a);
##title('Z-Plane');
##set(findobj(gca, 'Type', 'line'), 'LineWidth', 2);
##grid on;

% 3

##H = @(z) 7./(1-2.*(z.^-1)+6.*(z.^-2));
##a     = [1, 2, 6];
##polos = roots(a);
##
##angulo_polo = angle(polos(1));
##f_pico_hz   = angulo_polo * (fm / (2*pi));
##radio       = abs(polos(1));
##
##fprintf('Polo: %.2f Hz\n', f_pico_hz);
##fprintf('Radio en el circulo: %.2f\n', radio);
##
##H_f = H(z);
##stemft_half(abs(H_f), frecuencias, fm);
##line([f_pico_hz, f_pico_hz], [0, max(abs(H_f))], 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1.5);

% 4

##
##H     = @(z) 1+1/2.*(z.^-1)+1/4.*(z.^-2)+1/8.*(z.^-3)+1/16.*(z.^-4)+1/32.*(z.^-5)+1/64.*(z.^-6)+1/128.*(z.^-7);
##b     = [1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128];
##ceros = roots(b);
##
##angulo_cero = angle(ceros(1));
##f_valle_hz  = angulo_cero * (fm / (2*pi));
##radio       = abs(ceros(1));
##
##fprintf('Polo: %.2f Hz\n', f_valle_hz);
##fprintf('Radio en el circulo: %.2f\n', radio);
##
##H_f = H(z);
##stemft_half(abs(H_f), frecuencias, fm);
##line([f_valle_hz, f_valle_hz], [0, max(abs(H_f))], 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1.5);
##



