import numpy as np
import matplotlib.pyplot as plt

def senoidal(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = np.sin(2 * np.pi * fs * t + fase)

    return t, x


fms = [100, 25, 10, 4, 1, 0.5]

fig, axs = plt.subplots(3, 2, figsize=(12, 10), sharex=True, sharey=True)

for ax, fm in zip(axs.flatten(), fms):
    t, x = senoidal(0, 1, fm, fs=5, fase=0)
    ax.stem(t, x, label=f"fm={fm} Hz")
    ax.set_title(f"Senoidal fm={fm} Hz")
    ax.set_xlabel("t [s]")
    ax.set_ylabel("amplitud")
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.show()

#En la frecuencia muestral de 100 Hz la cantidad de ciclos
#corresponde a 5 Hz
#En los casos de fm 4, 1 y 0.5 Hz la discrepancia puede ser
#porque no se cumple la igualdad 2*fs <= fm
#Para 10 y 25, se cumple la igualdad, pero la frecuencia de
#muestreo no es suficiente para mostrar correctamente los 5 ciclos