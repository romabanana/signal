close all;
clear;
clc;

fm = 15000;
N = 1024;
t = (0:N-1)/fm;

## Vector de frecuencias
f = zeros(1,N);
for k = 0:N-1
    if k < N/2
        f(k+1) = k*fm/N;
    else
        f(k+1) = (k-N)*fm/N;
    endif
endfor

## Respuesta ideal en frecuencia
H = zeros(1,N);
for k = 1:N
    fk = abs(f(k));
    ## Banda [100,200]
    if fk >= 100 && fk <= 200
        H(k) = 1;
    endif
    ## Banda [1640,3028]
    if fk >= 1640 && fk <= 3028
        H(k) = 1;
    endif
    ## Banda [5000,6000]
    if fk >= 5000 && fk <= 6000
        H(k) = (fk - 5000)/(6000 - 5000);
    endif

endfor

figure(1);
plot(f,H,'k','LineWidth',1.5);
title('Respuesta ideal en frecuencia');
xlabel('Frecuencia [Hz]');
ylabel('|H(f)|');
grid on;
xlim([-6500 6500]);

## Respuesta al impulso ideal
h_ideal = real(ifft(H));

## Centrar
h_ideal = [h_ideal(N/2+1:N) h_ideal(1:N/2)];

figure(2);
plot(h_ideal);
title('Respuesta al impulso ideal');
xlabel('n');
ylabel('h[n]');
grid on;
