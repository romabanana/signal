function y = convocir(x, h, n)
    if nargin < 3
        n = max(length(x), length(h));
    endif

    x_pad = [x, zeros(1, n - length(x))];
    h_pad = [h, zeros(1, n - length(h))];

    y = zeros(1, n);

    for i = 1:n
        for j = 1:n
            idx = mod(i - j, n) + 1;
            y(i) = y(i) + x_pad(idx) * h_pad(j);
        endfor
    endfor
endfunction
