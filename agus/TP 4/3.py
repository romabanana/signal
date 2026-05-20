import numpy as np
import matplotlib.pyplot as plt

def fourier(s):
    S = np.zeros(len(s), dtype=complex)
    for k in range(len(s)):
        for n in range(len(s)):
            S[k] += s[n] * np.exp(-2j * np.pi * k * n / len(s))
    return S

t = np.arange(0, 1, 1/100)
s = np.sin(2*np.pi * 10 * t)

S = fourier(s)
#Aplicacion del retardo
retardo = 10
for k in range(len(S)):
    S[k] *= np.exp(-2j * np.pi * k * retardo / len(S))

#Antitransformacion
anti_s = np.zeros(len(s), dtype=complex)
for k in range(len(s)):
    for n in range(len(s)):
        anti_s[k] += S[n] * np.exp(2j * np.pi * k * n / len(s))
anti_s /= len(s)

plt.stem(t, s, 'blue', label='Señal original')
plt.stem(t, anti_s.real, 'red', label='Señal reconstruida')
plt.title("Transformada de Fourier y su inversa")
plt.legend()
plt.show() #se ve la señal roja desplazada 10 muestras a la derecha