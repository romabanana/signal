function w = window(t, y, p1, p2)
  w = 0.*t;
  n = length(w);
  if p2 <= n
    w(p1:p2) = y(p1:p2);
  else
    w(p1:end) = y(p1:end);
  endif

endfunction
