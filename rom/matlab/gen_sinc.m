function [x, y] = gen_sinc(tini, tfin, fm , fs, fase)
    T = 1/fm;
    t = tini:T:tfin-T;
    x = (2*pi*fs*t) + fase;
    y = sin(x) ./ (x + (x==0)) + (x==0);
end
