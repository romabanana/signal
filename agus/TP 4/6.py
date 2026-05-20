import numpy as np
import matplotlib.pyplot as plt

def fourier(s):
    S = np.zeros(len(s), dtype=complex)
    for k in range(len(s)):
        for n in range(len(s)):
            S[k] += s[n] * np.exp(-2j * np.pi * k * n / len(s))
    return S

def frecuencias(fm, N):
    freq = np.zeros(N)
    for k in range(N):
        if k < N//2:
            freq[k] = k * fm / N
        else:
            freq[k] = (k - N) * fm / N #para representar la simetria de frecuencias
    return freq

signal = np.loadtxt('TP 4 - datasets/necg.txt')
S = fourier(signal)

#creo el vector de frecuencias
freq = frecuencias(360, len(signal))

S_filtered = np.copy(S)
for k in range(len(signal)):
    if 40 <= abs(freq[k]) <= 180:
        S_filtered[k] = 0

anti_signal = np.zeros(len(signal), dtype=complex)
for k in range(len(signal)):
    for n in range(len(signal)):
        anti_signal[k] += S_filtered[n] * np.exp(2j * np.pi * k * n / len(signal))
anti_signal /= len(signal)

plt.plot(signal, 'blue', label='Señal original')
plt.plot(anti_signal.real, 'red', label='Señal filtrada')
plt.show()