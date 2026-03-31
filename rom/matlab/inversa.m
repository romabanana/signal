# Creo que es la correcta...
function [t, y] = gen_sen_inversa(tini, tfin, fm , fs, fase)
    T = 1/fm;
    t = tini:T:tfin-T;
    x = 2*pi*fs*t;
    y = asin(x + fase);
end
