function [y] = normp(x, p)

  N = length(x);
  y = 0;
  for i=1:N
    y += x(i)^p;
  endfor
  y = y^(1/p);

  endfunction

