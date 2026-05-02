function y = convo(a, b)

    # muestras = n + m -1
    n = length(a) + length(b) - 1;

    # incializo/completo vectores
    y = zeros(1,n);
    a=[ a,zeros(1,n-length(a)) ];
    b=[ b,zeros(1,n-length(b)) ];

    for (i=1:n)
      for (j=1:i)
        y(i) += a(i-j+1)*b(j);
      endfor
    endfor

endfunction
