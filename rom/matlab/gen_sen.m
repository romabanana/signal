function [t, y] = gen_sen(tini, tfin, fm , fs, fase)
    T = 1/fm;
    t = tini:T:tfin-T;
    x = 2*pi*fs*t;
    y = sin(x + fase);    
end
