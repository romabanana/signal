function v = varianza(y, m)
    N = length(y);
    m = (sum((y.-m).^2))*(1/(N-1));
end
