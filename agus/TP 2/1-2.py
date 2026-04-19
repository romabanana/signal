import numpy as np
import matplotlib.pyplot as plt

#y[n] = sqrt(x[n]^2 - 2 * x[n-1]*x[n] + x[n-1]^2)

x = np.arange(0, 10)  # Señal de entrada (puede ser cualquier señal discreta)
#x = np.array([0, 1, 2, 4, 8, 16, 32])  # Ejemplo de señal de entrada
#x = np.array([0, 1, 3, 7, 4, 13, 15])  # Ejemplo de señal de entrada
y = np.zeros(len(x))
for n in range(len(x)):
    if n == 0:
        y[n] = 0  # Para n=0, no hay x[n-1], se asume x[-1]=0
    else:
        y[n] = np.sqrt(x[n]**2 - 2 * x[n-1]*x[n] + x[n-1]**2)

plt.stem(y)
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Salida del sistema')
plt.show()