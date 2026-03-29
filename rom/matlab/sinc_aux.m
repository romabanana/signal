function y = sinc_aux(t)
  y = sin(t) ./ (t + (t==0)) + (t==0);

  end

