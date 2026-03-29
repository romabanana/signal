function y = sinc_aux3(t)
  fs = 0.5; #asi dice el tp...
  fm = 10;
  ti = t(1);
  tf = t(end) + 1/fm;
  phi = 0;

  [_, y] = gen_sinc(ti, tf, fm, fs, phi);
  end

