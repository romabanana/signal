function y = impulso(a, b, N)
  % Parámetros
  % Número de muestras a calcular
  y = zeros(1, N);  % Pre-asignamos memoria para la salida
  x = [1, zeros(1, N-1)]; % Creamos el impulso unitario delta[n]

  % Implementación del bucle recursivo
  for n = 1:N
      % y[n] = x[n] + y[n-2]
      % Nota: En MATLAB los índices empiezan en 1, así que n-2 es (n-2)

      term_x = x(n);

      % Manejo de condiciones iniciales (evitar índices menores a 1)
      if n > 2
          term_y_past = y(n-2);
      else
          term_y_past = 0;
      end

      y(n) = term_x + term_y_past;
  end

  stem(0:N-1, y, 'filled');

endfunction
