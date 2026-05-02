function [t, y] = gen_cl_sen10_alt(ti, tf, fm, fs, coef)
  # inicializo
  y = zeros(1, fm); % !

  # fases
  fases = linspace(0, 2*pi, 10);

  for i = 1:10
    [_, seno] = gen_sen(ti, tf, fm, fs, fases(i));
    y         = y + coef(i) .* seno;
  endfor

  #t
  t = ti: 1/fm: tf - 1/fm;
endfunction
