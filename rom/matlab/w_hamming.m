function w = w_hamming(N)
  w = zeros(1, N);

  for n = 0:N-1
    w(n+1) = 0.54 - 0.46 * cos(2 * pi * n / (N-1));
  endfor
endfunction
