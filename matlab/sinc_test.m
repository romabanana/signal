t = linspace(-10, 10, 1000);

y1 = sinc(t);
y2 = sin(t)./t;
y2(t==0) = 1;

plot(t, y1, 'b'); hold on;
plot(t, y2, 'r');
legend("sinc (Octave)", "sin(t)/t");
grid on;
