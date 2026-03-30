import numpy as np
import matplotlib.pyplot as plt

def senoidal(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = np.sin(2 * np.pi * fs * t + fase)

    return t, x

def sync(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)

    x = 2 * np.pi * fs * t    
    syncx = np.where(x != 0, np.sin(x)/x, 1)


    return t, syncx

def cuad(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    c = np.where(np.mod(2 * np.pi * fs * t + fase, 2 * np.pi) >= np.pi, -1, 1)

    return t, c


plt.rcParams['axes.grid'] = True

t, x = senoidal(0, 1, 100, 5, 0)
plt.stem(t, x)
plt.show()

t, x = sync(-1, 1, 100, 5, 0)
plt.stem(t, x)
plt.show()

t, x = cuad(0, 1, 100, 5, 0)
plt.stem(t, x)
plt.show()