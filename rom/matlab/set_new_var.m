# z -> N(0,1) señal de entrada
# v -> varianza target
function x = set_new_var(z, v)
  # queremos mantener la media = 0
  #m = media(z);
  sqrt_v = sqrt(v);

  x = sqrt_v * z;


  endfunction
