ti = 0;
tf = 1;
r = 10;


media_de_medias = zeros(6,1);
media_de_varianzas = zeros(6,1);
fm = [5 10 50 100 150 200 300 400];

for j = 1:length(fm)
  medias = zeros(length(t),1);
  varianzas = zeros(length(t),1);
  [t, y] = gen_aleatoria(ti, tf, fm(j), r);
  for i = 1:length(t)
      columna = y(i,:);
      medias(i) = media(columna);
      varianzas(i) = var(columna);
  endfor
  media_de_medias(j) = media(medias)
  media_de_varianzas(j) = media(varianzas)

endfor
grid on;
hold on;
plot(1:length(fm),media_de_medias);
plot(1:length(fm),media_de_varianzas);

