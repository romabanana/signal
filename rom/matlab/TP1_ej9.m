clear all;
# Part One
%
A = 5;
fs = 10;
phi = 0.25*pi;
fm = 400;
ti = 0;
tf = 2;
N  = 16;

% Genera la señal
[t, y] = gen_sen(ti, tf, fm, fs, phi);  % Deterministica y Discreta
y = A*y; % multiplica por la amplitud

% Cuantización
y_modificada = cuantizar(rectificar(y), N, A/(N-1), @round);

% Ploteo
plot_type = 0; % 0 -> subplot; 1 -> overlay;
figure(1);
plott(plot_type, t, [y; y_modificada]);

# Part Two
%Varianzas
var1 = 2;
var2 = 0.1;

% "Tener en cuenta que en el contexto del ruido, la varianza mide cuanto se
% dispersan los valores del ruido respecto a la media. Por lo que si la varianza
% es baja el ruido será de baja intensidad, mientras que si es alta el ruido
% tendrá valores más altos, afectando en mayor medida a la señal útil

[_, ruido_1] = gen_aleatoria_alt(ti, tf, fm, 1, var1); % una realizacion
[_, ruido_2] = gen_aleatoria_alt(ti, tf, fm, 1, var2); % una realizacion

% Sumo
y_ruido_1 = y_modificada + ruido_1';
y_ruido_2 = y_modificada + ruido_2';

% Ploteo
##figure(2);
##plot(t, ruido_1);
##figure(3);
##plot(t, ruido_2);

% Calculo de alpha para SNR de 6db para ruido_1

potencia_y       = potencia(y_modificada);
potencia_ruido_1 = potencia(ruido_1);
#potencia_ruido_2 = potencia(ruido_2);

%Para SNR de 6dB -> Ps/Pr = 3.9811
%                   Ps/a²Pr0 = 3.9811
%                   Ps/3.9811Pr0 = a²
%                   sqrt(Ps/3.9811Pr0) = a
%

omega = 3.9811;
alpha = sqrt(potencia_y/(omega*potencia_ruido_1));
nueva_potencia_ruido_1 = alpha * alpha * potencia_ruido_1;
db = 10*log10(potencia_y/nueva_potencia_ruido_1) # ~ 6db

% Ploteo
##figure(4);
##stem(t, y_ruido_1);
##figure(5);
##stem(t, y_ruido_2);

# Part Three

% Animacion para ver la diferencia niveles
##figure(6);
##niveles = 16:-1:1;
##for n = niveles
##  y_modificada = cuantizar(rectificar(y), n, A/(n-1), @round);
##
##  plot(t,rectificar(y));
##  hold on;
##  stem(t, y_modificada);
##  hold off;
##  grid on;
##  axis([0, 0.2, -1, 10]);
##
##  pause(1);
##  clc;
##  endfor
##





