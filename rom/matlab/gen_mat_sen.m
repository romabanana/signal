function A = gen_mat_sen(fs, fm = 11025, n = 3000, n_fases = 8)
  A     = zeros(n_fases, n); %incializo la matrix
  fases = linspace(0, 2*pi, n_fases); % defino vector de fases;
  tm    = 1/fm;

  for i = 1:n_fases
    [_, A(i,:)] = gen_sen(0, tm * n, fm, fs, fases(i));
  endfor


endfunction
