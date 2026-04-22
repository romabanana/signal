import numpy as np
import matplotlib.pyplot as plt


#///////////////////1//////////////////////#
#y[n] = g[n] * x[n] -> g[n] = A*sin(w*n*T), con A constante, w = 2*pi*f y T periodo de muestreo
#y[n] = A*sin( (2*pi*f) *n*T) * x[n]

#Causal, la salida no depende de entradas futuras
#Lineal, se cumple seperposicion y homogeneidad (a*y = a*x y y1+y2 = x1+x2)
#Variante en el tiempo, el coeficiente g[n] varía con el tiempo
#Sin memoria, no depende de entradas anteriores
#No invertible, una misma salida puede ser generada por diferentes entradas
#Estable, y = A * sin(algo) * x -> |y| <= A * x por |sin(algo)| <= 1



x = np.arange(0, 100)  # Señal de entrada (puede ser cualquier señal discreta)
A = 3
f = 1
T = 0.1
y = A * np.sin(2 * np.pi * f * np.arange(len(x)) * T) * x

plt.stem(y)
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Salida del sistema 1')
plt.show()

#///////////////////2//////////////////////#
#y[n] = sum(k=n-no, n+no) x[k]

#No causal
#Lineal
#Invariante en el tiempo
#Con memoria
#No invertible, se calcula un promedio
#Estable, |y| <= (2*no+1) * max(|x|)


x = np.arange(0, 100)  # Señal de entrada (puede ser cualquier señal discreta)
no = 2
y = np.zeros(len(x))
for n in range(len(x)):
    if n < no:
        y[n] = np.sum(x[:n+no+1])  # Suma desde k=0 hasta n+no
    elif n >= len(x) - no:
        y[n] = np.sum(x[n-no:])  # Suma desde k=n-no hasta el final de x
    else:
        y[n] = np.sum(x[n-no:n+no+1])  # Suma desde k=n-no hasta n+no

plt.stem(y)
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Salida del sistema 2')
plt.show()

#///////////////////3//////////////////////#
#y[n] = x[n] + 2

#Causal
#No lineal, porque y(0) =! 0
#Invariante en el tiempo
#Sin memoria
#Invertible
#Estable, |y| <= |x| + 2


x = np.arange(0, 100)  # Señal de entrada (puede ser cualquier señal discreta)
y = x + 2

plt.stem(y)
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Salida del sistema 3')
plt.show()

#///////////////////4//////////////////////#
#y[n] = n * x[n]

#Causal
#Lineal
#Variante en el tiempo
#Sin memoria
#Invertible para n =! 0
#No estable, n puede crecer al infinito


x = np.arange(0, 100)  # Señal de entrada (puede ser cualquier señal discreta)
y = np.arange(len(x)) * x

plt.stem(y)
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Salida del sistema 4')
plt.show()