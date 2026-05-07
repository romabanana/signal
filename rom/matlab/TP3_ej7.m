# Parte I

ph = 0;
fm = 1000;
N  = 500;
fs = 100;
ti = 0;
tf = 5;
r  = 1;
v  = 0.5;

# Genero x[n]
[t, comp_1] = gen_aleatoria_alt_fix(ti, tf, fm , r, v);
[_, comp_2] = gen_sen(ti, tf, fm, fs, ph);

x           = comp_1 + comp_2; % !

##plot(t,x);
norma_2 = normp(x, 2)
energia = norma_2 ^ 2
RMS     = norma_2 / sqrt(N)
accion  = normp(x, 1)
Amp     = max(abs(x))

# Parte II

[_, y]           = gen_sen(ti, tf, fm, fs, ph);
producto_interno = dot(x,y)
tita_rad         = producto_interno/(norm(x)*norm(y))
tita_deg         = rad2deg(tita_rad)

# bastante parecidas, no identicas.

# Parte III
fs_2       = 200;
[_, phi_1] = gen_sen(ti, tf, fm, fs, ph);
[_, phi_2] = gen_sen(ti, tf, fm, fs_2, ph);

phi_1      = phi_1 ./ (norm(phi_1)); %normañzo
phi_2      = phi_2 ./ (norm(phi_2));


alpha_1 = dot(x, phi_1); % ~ 1
alpha_2 = dot(x, phi_2); % ~ 0

x_aprox = alpha_1 * phi_1 + alpha_2 * phi_2;

w   = x - x_aprox;
ecm = normp(w, 2)^2

##relative_error = norm(x - x_aprox)^2 / norm(x)^2;
# A partir del error relativo se obtiene 50%...

# Parte IV

phase_nueva      = pi/2;
[_, y]           = gen_sen(ti, tf, fm, fs, phase_nueva);
y_desfasada      = dot(x,y)
tita_rad         = producto_interno/(norm(x)*norm(y))
tita_deg         = rad2deg(tita_rad)

# El producto pasa a ser ~ 0 al cambiar la fase.
# En efecto sin(tita) y sin(tita + pi/2) son sin y cos.
# Y las areas positivas de una se cancelan con las negativas de la otra
# (o con cero)..
