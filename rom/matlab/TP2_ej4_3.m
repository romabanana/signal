#Sistema: y[n] - 0.5 y[n-1] + 0.25 y[n-2] = x[n]
% Coeficientes:
b = [1, 0, 0];
a = [1, -0.50, 0.25];

cant_muestras = 20;
x = zeros(1, cant_muestras);
x(1) = 1; % delta[0] = 1

h = zeros(1, cant_muestras);

% Resolvemos la ecuación en diferencias muestra por muestra: h[n] = h[n-2] + x[n]
% Empezamos en n=3 para evitar índices negativos o fuera de rango en Octave (que arranca en 1)
h(1) = x(1); % n = 0 -> h[0] = 0 + x[0] = 1
h(2) = 0.5; % n = 1 -> h[1] = 0 + x[1] = 0

for n = 3:cant_muestras
    h(n) = 0.5  * h(n-1) - 0.25 * h(n-2) - x(n);
end
stem(h)
