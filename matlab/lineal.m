function y = lineal(t)
  y = (t >= 0) .* (t < 1) .* (1 - abs(t));
end

