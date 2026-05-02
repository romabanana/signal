function [t, y] = gen_aleatoria_fix(tini, tfin, fm , r)
    T = 1/fm;
    t = tini:T:tfin-T;
    n = length(t);
    y = randn(n, r);
    y = y';
end
