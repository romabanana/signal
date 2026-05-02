# Aproximacion de Funciones...

# Defino función a aproximar
t = -1:0.01:1;
y = -1 .* (t < 0) + 1 .* (t >= 0);


# Funciones Auxiliares

# Polinomio de Lagrendre grado 4
function y = legendre4(a1,a3)
    x = -1:0.01:1;
    y  = a1 .* ( sqrt(3/2) .* x) + a3 .* ( sqrt(7/2) .* (((5/2).*x.^3) - (3/2).*x));
endfunction

# Polinomio de Lagrendre grado 6
function y = legendre6(a1,a3,a5)
    x = -1:0.01:1;
    y  = a1 .* ( sqrt(3/2) .* x) + a3 .* ( sqrt(7/2) .* (((5/2).*x.^3) - (3/2).*x))+ a5.* (sqrt(11/2) .* ((63/8 .*x.^5) - (35/4 .*x.^3) + (15/8 .*x)));
endfunction

# Error Cuadratico MEdio
function x = ecm(y, yi)
    w = y - yi;
    x = 0;
    l = length(w);
    for i=1:l
      x+= w(i)^2;
    endfor
endfunction

# Retorna un vector con paso 0.1 en [x-1, x+1]
function y = variar(x)
  y = [[x-1:0.1:x] [x+0.1:0.1:x+1]];
endfunction


# Aplica variaciones y cálcula ecm para lagrendre 4.

a = variar(sqrt(3/2));
b = variar(- sqrt(7/32));

for i=1:21
  for j=1:21
    ECM_4(i,j) = ecm(y,legendre4(a(i),b(j)));
  endfor
endfor


# Aplica variaciones y cálcula ecm para lagrendre 6.
c = variar(sqrt(11/128));

for i=1:21
  for j=1:21
    ECM_6(i,j) = ecm(y,legendre6(a(i),b(j),c(j)));
  endfor
endfor

# Coeficientes Correctos

aideal = sqrt(3/2);
bideal = - sqrt(7/32);
cideal = sqrt(11/128);

y1 = legendre4(aideal, bideal);         # 1)
y2 = legendre6(aideal, bideal, cideal); # 3)


figure(1);
hold on
plot(t,y);
plot(t,y1);
plot(t,y2);
title("y(x) y aproximaciones");
legend("y(x)","Polinomio de Legendre orden 3","Polinomio de Legendre orden 5",'location', 'southeast');
legend();
hold off;

e4 = ecm(y,y1); #ECM con Lagrendre 4 1)
e6 = ecm(y,y2); #ECM con Lagrendre 6 3)


figure(2);
mesh(ECM_4); # 2)
title(["ECM en aproximación con 4 coeficientes, mínimo = ", num2str(e4)]);


figure(3);
mesh(ECM_6); # 2)
title(["ECM en aproximación con 6 coeficientes, mínimo = ",num2str(e6)]);
