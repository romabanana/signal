pkg load signal;
# y[n] - 0.8y[n-1] + 0.12y[n-2] = x[n] + 0.5x[n-1]
# Y(z) - 0.8 z^-1 Y(z) + 0.12 z^-2 Y(z) = X(z) + 0.5 z^-1 X(z)
# Y(z) (1 - 0.8 z^-1 + 0.12 z^-2) = X(z) (1 + 0.5 z^-1)
# H(z) = Y(z)/ X(z) = (1 + 0.5 z^-1)/(1 - 0.8 z^-1 + 0.12 z^-2)

#Parte1
a = [1 -0.8 0.12];
b = [1 0.5];

zeros = roots(b) # 0 extra en 0...
polos = roots(a)

#EStabel porque todos los polos se hallan detnro del circulo unitario
##zplane(b,a);

#parte2
fm = 1000; %(1kHz)
N = 150; # numero de puntos
w = linspace(0, 2*pi, N); #circulo
z = exp(1i * w); #si r = 1 -> Z es equivalente a TFTD
frecuencias = (w / (2*pi)) * fm;



H = @(z) (1 + 0.5 .* z.^-1) ./ (1 - 0.8 .* z.^-1 + 0.12 .* z.^-2);
H_f = H(z);

##figure(2);
##stemft_half(abs(H_f), frecuencias, fm);
##figure(3);
##plot(angle(H_f))
#Aproxima um pb..

##cant_muestras = 30;
##[h, n] = impz(b, a, cant_muestras);
##figure(4);
##stem(n, h, 'filled', 'LineWidth', 1.5);
##title('Respuesta al Impulso usando impz()');
##xlabel('Muestras (n)');
##ylabel('h[n]');
##grid on;

#Peter III
## H = 1 / (s + 1)
## Euler: s = (1 - z^-1) / T
## Reemplazo:
## H = 1 / ((1 - z^-1) / T) + 1
## H = T / (1 - z^-1 + T)
## con T = 0.1:
## H = 0.1 / (1 - z^-1 + 0.1) = 0.1 / (1.1 - z^-1) = Y(z) / X(z)
## (1.1 - z^-1)Y(z) = 0.1X(z)
## Pasado al dominio temporal:
## 1.1y[n] - y[n-1] = 0.1x[n]
##
## Despejando:
## y[n] = (1/1.1)y[n-1] + (0.1/1.1)x[n]
Hs    = @(s)  1 ./ (s + 1 );
euler = @(z,T) Hs((1-z.^-1)/T);

T  = 0.1;
N  = 1000;

w_digital = linspace(0, pi, N);

fm = 1/T;
frecuencias_hz = (w_digital / (2*pi)) * fm;

% Omega = 2 * pi * f
w_analoga = 2 * pi * frecuencias_hz;

E_digital = abs(euler(exp(w_digital.*1i), T));
E_analoga = abs(Hs(w_analoga .* 1i));




#Peter IV
## H = 1 / (s + 1)
## bilineal: s = (2/T) * (1 - z^-1)/(1 + z^-1)
## Reemplazo:
## H = 1 / ((2/T) * (1 - z^-1)/(1 + z^-1) + 1)
## Multiplicando numerador y denominador por (1 + z^-1):
## H = (1 + z^-1) / ((2/T)(1 - z^-1) + (1 + z^-1))
## con T = 0.1:
## H = (1 + z^-1) / (20(1 - z^-1) + (1 + z^-1))
## H = (1 + z^-1) / (21 - 19z^-1)
## H(z) = Y(z) / X(z)
## (21 - 19z^-1)Y(z) = (1 + z^-1)X(z)
## Pasado al dominio temporal:
## 21y[n] - 19y[n-1] = x[n] + x[n-1]
## Despejando:
## y[n] = (19/21)y[n-1] + (1/21)x[n] + (1/21)x[n-1]
## y[n] = 0.9048y[n-1] + 0.0476x[n] + 0.0476x[n-1]
bilineal = @(z,T) Hs((2/T).*((1-z.^-1)./(1 + z.^-1))); #bilineal
E_digital_b = abs(bilineal(exp(w_digital.*1i), T));

figure(6);
plot(frecuencias_hz, E_analoga, 'k--', 'LineWidth', 2);
hold on;
plot(frecuencias_hz, E_digital, 'r', 'LineWidth', 1.5);
plot(frecuencias_hz, E_digital_b, 'b', 'LineWidth', 1.5);
hold off;
title('Comparación de Respuesta en Magnitud: Analógico vs. Euler');
xlabel('Frecuencia [Hz]');
ylabel('|H(f)|');
legend('Filtro Analógico Ideal H(s)', 'Filtro Digitalizado H(z) (Euler)', 'Filtro Digitalizado H(z) (Bilineal)','Location', 'northeast');
grid on;
xlim([0 fm/2]);

