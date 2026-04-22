import numpy as np
import matplotlib.pyplot as plt

delta = np.zeros(10)
delta[0] = 1  # Impulso unitario


#////////////////////1//////////////////////#
#y[n] - y[n-2] = x[n]
#y[n] = x[n] + y[n-2]

#a = [1, 0, -1]
#b = [1]

h = np.zeros(len(delta))
for n in range(len(delta)):
    if n >= 2:
        h[n] = delta[n] + h[n-2]
    else:
        h[n] = delta[n]
print("Respuesta al impulso del sistema 1:", h)
#IIR, autorregresivo

#////////////////////2//////////////////////#
#y[n] = x[n] + 0.5*x[n-1]

h = np.zeros(len(delta))  # Respuesta al impulso del sistema
for n in range(len(delta)):
    if n >= 1:
        h[n] = delta[n] + 0.5 * delta[n-1]
    else:
        h[n] = delta[n]
print("Respuesta al impulso del sistema 2:", h)
#FIR, promedio movil (no hay retroalimentacion)


#////////////////////3//////////////////////#
#y[n] - 0.5 *y[n-1] + 0.25*y[n-2] = x[n]
#y[n] = x[n] + 0.5 *y[n-1] - 0.25*y[n-2]

h = np.zeros(len(delta))  # Respuesta al impulso del sistema
for n in range(len(delta)):
    if n >= 2:
        h[n] = delta[n] + 0.5 * h[n-1] - 0.25 * h[n-2]
    else:
        h[n] = delta[n]
print("Respuesta al impulso del sistema 3:", h)
#IR, autorregresivo


"""""
Funcion utilizando a y b representando las partes de entrada y salida del sistema
a = [1, 0, -1]
b = [1]

N = 10
delta = np.zeros(N)
delta[0] = 1

h = np.zeros(N)

for n in range(N):
    # Parte entrada
    suma_x = 0
    for k in range(len(b)):
        if n-k >= 0:
            suma_x += b[k] * delta[n-k]

    # Parte salida previa
    suma_y = 0
    for k in range(1, len(a)):
        if n-k >= 0:
            suma_y += a[k] * h[n-k]

    h[n] = (suma_x - suma_y) / a[0]

"""""