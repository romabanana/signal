function [t, y] = gen_cuad(tini, tfin, fm , fs, fase)
    T = 1/fm;
    t = tini:T:tfin-T;
    x = 2*pi*fs*t + fase;
    modulo = mod(x,(2*pi));
    y = -(modulo >= pi) + (modulo<pi);
end
