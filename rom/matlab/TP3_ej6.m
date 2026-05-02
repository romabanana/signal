[tonos, fm_tonos] = audioread('escala.wav');

n_tonos    = length(tonos);
n_por_tono = floor(n_tonos/8); % equispaciados


FS_LA   = 440;
mat_LA = gen_mat_sen(FS_LA, fm_tonos, n_por_tono);

cant_tonos = 8;
for i =1:cant_tonos
  idx_begin = ((i - 1) * n_por_tono) + 1;
  idx_end   = i * n_por_tono;
  tono      = tonos(idx_begin: idx_end);
  P(i)      = max(mat_LA * tono);
endfor

[_, pos] = max(P);
display(['El La esta en la posicion :', num2str(pos)]);
