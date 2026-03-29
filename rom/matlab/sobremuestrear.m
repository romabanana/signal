function [mt, y] = sobremuestrear(original, ti, tf, fm, m, interpolador)

  n = length(original);
  tm = 1/fm;
  nt = ti:tm:tf-tm; ##

  T4 = tm/m;
  mt = ti:T4:tf-T4;

  y = zeros(length(mt), 1);

  for k = 1:length(mt)
    for i = 1:n
      y(k) = y(k) + original(i) * interpolador((mt(k) - nt(i)) / tm);
    endfor
  endfor

end
