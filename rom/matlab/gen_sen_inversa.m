
function [t, y] = gen_sen_inversa(tini, tfin, fs)
##    % fs = Sampling frequency (e.g., 1000)
##    % tini/tfin = Time range (e.g., 0 to 1)
##
##    t = tini : 1/fs : tfin;
##
##    % Create a signal that stays between -1 and 1
##    % For example, a linear ramp from -1 to 1
##    input_signal = linspace(-1, 1, length(t));
##
##    % Now we can safely take the arcsin
##    y = asin(input_signal);
end
