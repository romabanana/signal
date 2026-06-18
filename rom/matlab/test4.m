% --- Configuración Inicial ---
Hs    = @(s)  1 ./ (s + 1 );
euler = @(z,T) Hs((1-z.^-1)/T);

T  = 0.1;
N  = 1000;

% 1. Vector de frecuencia digital (de 0 a Nyquist)
w_digital = linspace(0, pi, N);

% 2. EL PUENTE: Convertimos los radianes digitales a Hz físicos
% Frecuencia de muestreo en Hz: fm = 1/T
fm = 1/T;
frecuencias_hz = (w_digital / (2*pi)) * fm;

% 3. EL PUENTE ANALÓGICO: Convertimos los Hz a frecuencias angulares continuas (Omega)
% Omega = 2 * pi * f
w_analoga = 2 * pi * frecuencias_hz;

% --- Cómputo de Respuestas en Frecuencia ---
% Filtro Digital (Evaluado en la circunferencia unitaria)
E_digital = abs(euler(exp(w_digital.*1i), T));

% Filtro Analógico (Evaluado en el eje imaginario continuo s = j*Omega)
E_analoga = abs(Hs(w_analoga .* 1i));


figure(1);
plot(frecuencias_hz, E_analoga, 'k--', 'LineWidth', 2);
hold on;
plot(frecuencias_hz, E_digital, 'r', 'LineWidth', 1.5);
hold off;
title('Comparación de Respuesta en Magnitud: Analógico vs. Euler');
xlabel('Frecuencia [Hz]');
ylabel('|H(f)|');
legend('Filtro Analógico Ideal H(s)', 'Filtro Digitalizado H(z) (Euler)', 'Location', 'northeast');
grid on;
xlim([0 fm/2]);
