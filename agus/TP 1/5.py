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

#Frecuencia aparente: fa = |fs - N*fm|, se prueba N = fs / fm = 4000 / 129 ≈ 31, lo que da fa = |4000 - 31*129| = 1 Hz
#Ademas, un ciclo tarda 1 segundo. f = 1 / T = 1 / 1 = 1 Hz
#Es decir, se observa una señal de 1 Hz porque la frecuencia de muestreo es insuficiente para representar correctamente la señal