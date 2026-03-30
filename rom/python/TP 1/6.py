import numpy as np
import matplotlib.pyplot as plt

def senoidal(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = np.sin(2 * np.pi * fs * t + fase)

    return t, x

def sinc_interp(x, t, ti, fs):
    xi = np.zeros(len(ti))

    for i in range(len(ti)):
        suma = 0
        for n in range(len(t)):
            mT, nT, T = ti[i], t[n], t[1] - t[0]
            tau = (mT - nT) / T
            
            arg = 2 * np.pi * fs * tau

            if arg == 0:
                valor = 1
            else:
                valor = np.sin(arg) / arg

            suma += x[n] * valor
        
        xi[i] = suma

    return xi

def step_interp(x, t, ti, fs):
    xi = np.zeros(len(ti))

    for i in range(len(ti)):
        suma = 0
        for n in range(len(t)):
            mT, nT, T = ti[i], t[n], t[1] - t[0]
            tau = (mT - nT) / T
        
            #arg = 2 * np.pi * fs * tau

            eps = 1e-9 #tolerancia para evitar problemas de precisión con valores muy cercanos a los limites
            if 0 <= tau + eps < 1:
                valor = 1
            else:
                valor = 0

            suma += x[n] * valor
        
        xi[i] = suma

    return xi

def line_interp(x, t, ti, fs):
    xi = np.zeros(len(ti))

    for i in range(len(ti)):
        suma = 0
        for n in range(len(t)):
            mT, nT, T = ti[i], t[n], t[1] - t[0]
            tau = (mT - nT) / T
        
            #arg = 2 * np.pi * fs * tau

            if np.abs(tau) < 1:
                valor = 1 - np.abs(tau)
            else:
                valor = 0

            suma += x[n] * valor
        
        xi[i] = suma

    return xi

plt.rcParams['axes.grid'] = True

fm = 10
fm_new = 40
T = 1 / fm
Ti = 1 / fm_new

t, x = senoidal(0, 1, fm, 0.5, 0)
ti = np.arange(0, 1, Ti)

xi = sinc_interp(x, t, ti, 0.5)
plt.stem(t, x, label="Original")
plt.plot(ti, xi, label="Interpolada (sinc)")
plt.legend()
plt.show()

xi_step = step_interp(x, t, ti, 0.5)
plt.stem(t, x, label="Original")
plt.plot(ti, xi_step, label="Interpolada (step)")
plt.legend()
plt.show()

xi_line = line_interp(x, t, ti, 0.5)
plt.stem(t, x, label="Original")
plt.plot(ti, xi_line, label="Interpolada (lineal)")
plt.legend()
plt.show()