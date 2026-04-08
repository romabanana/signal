import numpy as np
import matplotlib.pyplot as plt

T = 1/800 #8 muestras en 0.01 segundos, 80 en 0.1 segundos, 800 en 1 segundo
A = 3
t_retardo = 5 / 800 #retardo de 5 muestras
fs = 20 # se completan dos fases
phi = -2 * np.pi * fs * t_retardo

t = np.arange(0, 0.1, T)
x = A * np.sin(2 * np.pi * fs * t + phi)
plt.stem(t, x)
plt.show()
