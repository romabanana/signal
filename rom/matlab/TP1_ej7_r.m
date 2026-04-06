ti = 0;
tf = 1;
fm = 50;

% Inicializo vectores
vector_de_medias = zeros(6,2);
vector_de_varianzas = zeros(6,2);
r = [5 10 50 100 150 200 300 400];

% En cada iteracion aumento las realizaciones
for j = 1:length(r)


  % Inicializo vectores
  medias_es = zeros(length(t),1);
  varianzas_es = zeros(length(t),1);

  medias_er = zeros(r(j),1);
  varianzas_er = zeros(r(j),1);
  % Genero señal estocastica
  [t, y] = gen_aleatoria(ti, tf, fm, r(j)); %r realizaciones
  y = y'; %coso

  % Para la Estacionariedad calculo los estidisticos por columna
  for i = 1:length(t)
      columna = y(:,i);
      medias_es(i) = media(columna);
      varianzas_es(i) = var(columna);
  endfor

  vector_de_medias(j,1) = media(medias_es);
  vector_de_varianzas(j,1) = media(varianzas_es);

  % Para la Ergocidad por fila
  for i = 1:r(j)
      fila = y(i,:);
      medias_er(i) = media(fila);
      varianzas_er(i) = var(fila);
  endfor

  vector_de_medias(j,2) = media(medias_er);
  vector_de_varianzas(j,2) = media(varianzas_er);



endfor


% Subplot 1: Medias
subplot(2,1,1);
hold on; grid on;
plot(r, vector_de_medias(:,1), '-o', 'LineWidth', 1.5, 'MarkerSize', 6); % Estacionaria
plot(r, vector_de_medias(:,2), '--s', 'LineWidth', 1.5, 'MarkerSize', 6); % Ergodica
title('Análisis de la Media (Mean)');
xlabel('Cant de Realizacions (r)');
ylabel('Valor de la Media');
legend('Media Estacionaria (Promedio de Columnas)', 'Media Ergódica (Promedio de Filas)', 'Location', 'best');

% Subplot 2: Varianzas (Variance)
subplot(2,1,2);
hold on; grid on;
plot(r, vector_de_varianzas(:,1), '-o', 'LineWidth', 1.5, 'Color', [0.85 0.33 0.1], 'MarkerSize', 6);
plot(r, vector_de_varianzas(:,2), '--s', 'LineWidth', 1.5, 'Color', [0.49 0.18 0.56], 'MarkerSize', 6);
title('Análisis de la Varianza');
xlabel('Cant de Realizacions (r)');
ylabel('Valor de la Varianza');
legend('Var Estacionaria', 'Var Ergódica', 'Location', 'best');

sgtitle('Propiedades Estadísticas vs. Frecuencia de Muestreo');
