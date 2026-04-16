import numpy as np
import matplotlib.pyplot as plt

def senoidal(tini, tfin, fm, fs, fase):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = np.sin(2 * np.pi * fs * t + fase)

    return t, x

def gen_random(fm):
    x = np.random.randn(fm)

    return x

def potency(x):
    return np.mean(x**2)

t, x = senoidal(0, 1, 100, 10, 0)
r = gen_random(100)
rx = x + r

plt.grid(True)
plt.stem(t, x, 'b-', label='Señal original')
plt.stem(t, rx.flatten(), 'r-', label='Señal con ruido')
plt.legend()
plt.show()

Ps = potency(x)
Pr = potency(r)
SNR = 10 * np.log10(Ps / Pr)

print(f"Potencia de la señal: {Ps}")
print(f"Potencia del ruido: {Pr}")
print(f"Relación señal a ruido (SNR): {SNR} dB")

##//////////////////////////////////////////////////////////////////////////////##
a = 2
ar = a * r

Par = potency(ar)
SNR_ar = 10 * np.log10(Ps / Par)

print(f"\nPotencia del ruido amplificado: {Par}")
print(f"Relación señal a ruido con ruido amplificado (SNR_ar): {SNR_ar} dB")


"""""
snr(db) = 10 * log(Ps / Par) -> Da 0 si log 1, entonces Ps = Par
|
|
V
Par = 1/N * E (a*r)^2 -> r es el ruido original, a es el factor de amplificación. E es la sumatoria, Par es la potencia del ruido amplificado. N es el número de muestras.
Par = 1/N * E (a)^2 * (r)^2 -> a es constante, entonces:
Par = a^2 * (1/N * E r^2) = a^2 * Pr -> siendo Pr la potencia del ruido original

Ps = Par
Ps = a^2 * Pr
a^2 = Ps / Pr
a = sqrt(Ps / Pr)
"""""

a = np.sqrt(Ps / Pr)
ar = a * r

Par = potency(ar)
SNR_ar = 10 * np.log10(Ps / Par)
print(f"\nFactor de amplificación para obtener SNR = 0 dB: {a}")
print(f"Potencia del ruido amplificado con factor a: {Par}")
print(f"Relación señal a ruido con ruido amplificado con factor a (SNR_ar): {int(SNR_ar)} dB")