function v = varianza(y, m)
    N = length(y);
    v = (sum((y - m).^2)) * (1 / (N - 1));
end
