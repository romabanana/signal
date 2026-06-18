clc;
fm = 300;
T  = 1/fm;
t  = 0:T:1-T;
N  = length(t);

[t, sin_20] = gen_sen(0, 1, fm , 20, 0);
[t, sin_50] = gen_sen(0, 1, fm , 50, 0);

entrada     = sin_20 + sin_50;

### Construyo H[k]
# dw = 2*pi/N;
# frecuencias
w1 = 2*pi*40/fm;
w2 = 2*pi*60/fm;

H = ones(1, N);
f = zeros(1, N);

for k = 0:N-1   % k = 0 !!
  if k < N/2      %[0,149]
    w = k * 2*pi/N;
    f(k+1) = k * fm/N;
  else                    %[-150,-1]
    w = (k - N) * 2*pi/N;
    f(k+1) = (k - N) * fm/N;
  endif

  #Anulo
  if abs(w) >= w1 && abs(w) <= w2
    H(k+1) = 0;
  endif
endfor

figure(1);
plot(fftshift(f), fftshift(H), 'k', 'LineWidth', 1.2);
xlim([-150 150]);
ylim([-0.1 1.1]);
grid on;

### Construyo h[n]
h_t = real(ifft(H));
#plot(t, h_t) ????
h_t = [h_t((N/2)+1:end), h_t(1:N/2)];
plot(t, h_t)

### Truncado Temporal
#Longitud de la ventana... impar mejor (muestra central);
N_ventanas = 81;
#Ventanas
ventana_rect     = w_rect(N_ventanas);
ventana_hanning  = w_hanning(N_ventanas);
ventana_hamming  = w_hamming(N_ventanas);
ventana_blackman = w_blackman(N_ventanas);

#Recorto h..
M = length(h_t);
centro = (M / 2) + 1; % 151
mitad  = floor((N_ventanas - 1) / 2); %floor?

ini = centro - mitad;
fin = centro + mitad;
h_recortada = h_t(ini:fin);

#Obtengo los bk..
b_rect = h_recortada .* ventana_rect;
b_hanning = h_recortada .* ventana_hanning;
b_hamming = h_recortada .* ventana_hamming;
b_blackman = h_recortada .* ventana_blackman;

#zero-fill

b_rect_aux    = zeros(1,N);
b_hanning_aux = zeros(1,N);
b_hamming_aux = zeros(1,N);
b_blackman_aux= zeros(1,N);

b_rect_aux(ini:fin)     = b_rect;
b_hanning_aux(ini:fin)  = b_hanning;
b_hamming_aux(ini:fin)  = b_hamming;
b_blackman_aux(ini:fin) = b_blackman;

#hay que acomodar..
b_rect_aux = [b_rect_aux((N/2)+1:end), b_rect_aux(1:N/2)];
b_hanning_aux = [b_hanning_aux((N/2)+1:end), b_hanning_aux(1:N/2)];
b_hamming_aux = [b_hamming_aux((N/2)+1:end), b_hamming_aux(1:N/2)];
b_blackman_aux = [b_blackman_aux((N/2)+1:end), b_blackman_aux(1:N/2)];

H_rect     = abs(fft(b_rect_aux));
H_hanning  = abs(fft(b_hanning_aux));
H_hamming  = abs(fft(b_hamming_aux));
H_blackman = abs(fft(b_blackman_aux));
plot(angle(b_blackman_aux))

##figure(2);
##hold on;
##plot(f, H_rect);
##plot(f, H_hanning);
##plot(f, H_hamming);
##plot(f, H_blackman);
##grid on;

figure(2);
hold on;

% hehehe
f_shifted = fftshift(f);

plot(f_shifted, fftshift(H_rect),     'r-',  'LineWidth', 1.5);
plot(f_shifted, fftshift(H_hanning),  'g--', 'LineWidth', 1.5);
plot(f_shifted, fftshift(H_hamming),  'b-.', 'LineWidth', 1.5);
plot(f_shifted, fftshift(H_blackman), 'm:',  'LineWidth', 2.0);
plot(f_shifted, fftshift(H), 'k', 'LineWidth', 1.0);

hold off;

title('Filtro FIR(N = 25 Taps)');
xlabel('Frecuencia [Hz]');
ylabel('|H(e^{j\omega})|');
xlim([-150 150]); % Focus on the full physical Nyquist range
ylim([-0.05 1.2]); % Leave a little headspace at the top
grid on;
legend('Rectangular Window', ...
       'Hanning Window', ...
       'Hamming Window', ...
       'Blackman Window', ...
       'Ideal Filter Template', ...
       'Location', 'southwest');

##

y   = convo(entrada, b_blackman); #M + N + 1 -> hay que recortar..
fix = floor(N_ventanas/2);
y   = y(fix+1 : fix+N);


figure(3);
hold on;
plot(t,y);
plot(t,entrada);
figure(4);
plot(f, abs(fft(y)));
figure(5);
plot(f, abs(fft(entrada)));



