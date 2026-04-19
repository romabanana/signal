import numpy as np
import matplotlib.pyplot as plt


#///////////////////1//////////////////////#
#y[n] = g[n] * x[n] -> g[n] = A*sin(w*n*T), con A constante, w = 2*pi*f y T periodo de muestreo
#y[n] = A*sin( (2*pi*f) *n*T) * x[n]

#Sin memoria, no depende de entradas anteriores
#No invertible, una misma salida puede ser generada por diferentes entradas
#Causal, la salida no depende de entradas futuras
#No estable? y tiende a infinito
#Variante en el tiempo, el coeficiente g[n] varía con el tiempo
#No lineal, la salida no es proporcional a la entrada

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

#Con memoria
#Inverible, si se ignoran los ultimos valores
#No causal
#No estable, la salida crece al infinito
#Invariante en el tiempo
#Lineal

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

#Sin memoria
#Invertible
#Causal
#No estable
#Invariante en el tiempo
#Lineal

x = np.arange(0, 100)  # Señal de entrada (puede ser cualquier señal discreta)
y = x + 2

plt.stem(y)
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Salida del sistema 3')
plt.show()

#///////////////////4//////////////////////#
#y[n] = n * x[n]

#Sin memoria
#Invertible
#Causal
#No estable
#Variante en el tiempo
#Lineal

x = np.arange(0, 100)  # Señal de entrada (puede ser cualquier señal discreta)
y = np.arange(len(x)) * x

plt.stem(y)
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Salida del sistema 4')
plt.show()