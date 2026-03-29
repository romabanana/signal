function y = sinc_aux2(t)
  y = sin(t*pi) ./ (t*pi + (t==0)) + (t==0);

  end

