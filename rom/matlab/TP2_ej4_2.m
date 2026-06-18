% Sistema: y[n] = x[n] + 0.5x[n-1]
b = [1, 0.5];
a = [1, 0];

cant_muestras = 10;
h = zeros(1, cant_muestras);
x = zeros(1, cant_muestras);
x(1) = 1;


for n = 1:cant_muestras
    if n == 1
        % h(1) = b1 * x(1)
        h(n) = b(1) * x(n);
    else
        % h(2) = b1 * x(2) + b2 * x(1)
        h(n) = b(1) * x(n) + b(2) * x(n-1);
    end
end
stem(h)
