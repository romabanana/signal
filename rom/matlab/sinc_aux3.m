function y = sinc_aux3(t)
  fs = 0.5; #asi dice el tp...
  fm = 10;
  ti = t;
  tf = t + 1;
  phi = 0;

  [_, aux] = gen_sinc(ti, tf, fm, fs, phi);
  y = aux(1);
end

