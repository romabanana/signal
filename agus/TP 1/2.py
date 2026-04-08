import numpy as np
import matplotlib.pyplot as plt

def inv_senoidal(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = np.sin(2 * np.pi * fs * (t) + fase) #x_nuevo(t) = x(-t) ??

    return -t, x[::-1] #devuelve la señal invertida

def rec_senoidal(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = np.sin(2 * np.pi * fs * t + fase)

    return t, np.abs(x) #devuelve la señal rectificada (absoluta)
    #return t, np.maximum(x, 0) #devuelve la señal rectificada (positiva)

def cu_senoidal(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = np.sin(2 * np.pi * fs * t + fase)

    N = 8 #número de niveles
    H = (np.max(x)-np.min(x)) / (N-1) #magnitud del cuanto basada en el rango de la señal

    x_alter = x - np.min(x) #desplaza la señal para que el mínimo sea 0
    x_cu = np.where(x_alter >= (N-1)*H, (N-1)*H, np.round(x_alter / H) * H) #cuantiza la señal
    x_cu = x_cu + np.min(x) #desplaza la señal de vuelta a su rango original

    return t, x_cu


plt.rcParams['axes.grid'] = True

t, x = inv_senoidal(0, 1, 100, 5, 0)
plt.stem(t, x)
plt.show()

t, x = rec_senoidal(0, 1, 100, 5, 0)
plt.stem(t, x)
plt.show()

t, x = cu_senoidal(0, 1, 100, 5, 0)
#plt.plot(t, np.sin(2*np.pi*5*t + 0), label='original')
plt.step(t, x, where='mid', label='cuantizada')
plt.legend(); plt.grid(True); plt.show()
