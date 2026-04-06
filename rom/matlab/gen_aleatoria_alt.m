% y esta en modo columna... no fila !!!!

% Setea nueva varianza v
function [t, y] = gen_aleatoria_alt(tini, tfin, fm , r, v)
    T = 1/fm;
    t = tini:T:tfin-T;
    n = length(t);
    y = randn(n, r);
    if v != 1
      y = set_new_var(y, v);
    endif

end
