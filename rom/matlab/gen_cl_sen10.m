function [t, y] = gen_cl_sen10(ti, tf, fm, coef, fase)
  # inicializo
  y = zeros(1, fm); % !

  for fs = 1:10
    [_, seno] = gen_sen(ti, tf, fm, fs, fase);
    y         = y + coef(fs) .* seno;
  endfor

  #t
  t = ti: 1/fm: tf - 1/fm;
endfunction
