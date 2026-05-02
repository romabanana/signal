import numpy as np
import matplotlib.pyplot as plt

N = 100
n = np.arange(N)


fs1 = 0.05  # Frecuencia de la señal
phi1 = 0 # Fase
A1 = 1 # Amplitud
x1 = A1 * np.sin(2 * np.pi * fs1 * n + phi1)

fs2 = 0.05  # Frecuencia de la señal
phi2 = 0 # Fase
A2 = 1 # Amplitud
x2 = A2 * np.sin(2 * np.pi * fs2 * n + phi2)

plt.plot(n, x1, 'b-', label='Señal 1')
plt.plot(n, x2, 'r-', label='Señal 2')
plt.legend()
plt.show()

#Grado de similitud
numerador = np.sum(x1 * x2)
denominador = np.sqrt(np.sum(x1**2) * np.sum(x2**2)) #Similitud cosenoidal
grado = numerador / denominador if denominador != 0 else 0
print("Grado de similitud:", grado) #Evalua si tienen la misma forma o desplazamiento, pero ignora escalados