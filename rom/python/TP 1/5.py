import numpy as np
import matplotlib.pyplot as plt

def senoidal(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = np.sin(2 * np.pi * fs * t + fase)

    return t, x

t, x = senoidal(0, 2, 129, 4000, 0)
plt.stem(t, x)
plt.show()

#Debido a la alta diferencia entre frecuencia de muestreo y
#frecuencia de la señal, en la figura solo se muestran dos ciclos,
#por lo que la frecuencia de la onda se deberia aproximar a 200 Hz