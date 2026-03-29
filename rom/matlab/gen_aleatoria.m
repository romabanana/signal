function [t, y] = gen_aleatoria(tini, tfin, fm , r)
    T = 1/fm;
    t = tini:T:tfin-T;
    n = length(t);
    y = randn(n, r);

end
