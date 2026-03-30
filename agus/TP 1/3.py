import numpy as np
import matplotlib.pyplot as plt

T = 0.001
A = 3
t_retardo = 0.005 # suponiendo que cada punto representa 0.001
fs = 20 # se completan dos fases
phi = -2 * np.pi * fs * t_retardo

t = np.arange(0, 0.1, T)
x = A * np.sin(2 * np.pi * fs * t + phi)
plt.stem(t, x)
plt.show()