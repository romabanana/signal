#wut
##Las se˜nales verifican que cuanto m´as concentrada est´a su energ´ıa en cier-
##ta regi´on del dominio temporal, m´as dispersa estar´a en el dominio frecuencial, y
##viceversa. Ejemplos extremos de esto son una se˜nal senoidal, que tiene su energ´ıa
##distribuida a lo largo de toda la se˜nal, pero en dominio frecuencial ´esta se concen-
##tra en la frecuencia de la misma, y un delta de Dirac, que en dominio temporal
##tiene toda su energ´ıa concentrada en un instante, pero en dominio frecuencial
##contiene todas las frecuencias. Explore esta propiedad utilizando ventanas tem-
##porales, m´as o menos concentradas alrededor de cierto tiempo, y calculando sus
##respectivas transformadas de Fourier.

fs_1       = 10;
tini       = 0;
tfin       = 1;
fm         = 100;
fase       = 0.0;

[t, s_a] = gen_sen(tini, tfin, fm , fs_1, fase);

w_s_a    = window(t, s_a, 1, 11);

figure(1);
hold on;
stem(t, s_a);
stem(t, w_s_a);

S_A   = fft(s_a);
W_S_A = fft(w_s_a);
figure(2);
hold on;
stemft(abs(S_A), t, fm);
stemft(abs(W_S_A), t, fm);
