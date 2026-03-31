function y = lineal2(t)
  y = (abs(t) < 1) .* (1 - abs(t));
end

