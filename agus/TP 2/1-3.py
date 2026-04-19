import numpy as np
import matplotlib.pyplot as plt

# y[n] - 0.5*y[n-1] + 0.25*y[n-2] = x[n]
# y[n] = x[n] + 0.5*y[n-1] - 0.25*y[n-2]

x = np.arange(0, 10)  # Señal de entrada (puede ser cualquier señal discreta)
y = np.zeros(len(x))
for n in range(len(x)):
    if n == 0:
        y[n] = x[n]  # Para n=0, no hay y[n-2], se asume y[-2]=0
    elif n == 1:
        y[n] = x[n] + y[n-1]  # Para n=1, no hay y[n-2], se asume y[-2]=0
    else:
        y[n] = x[n] + 0.5 * y[n-1] - 0.25 * y[n-2]

plt.stem(y)
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Salida del sistema')
plt.show()