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

#Inicial
fm = 1/0.001
t = np.arange(0, 1, 1/fm)
s = np.sin(2 * np.pi * 10 * t) + 4*np.sin(2*np.pi * 20 * t)

#1
S = fourier(s)
freq = frecuencias(fm, len(s))

plt.stem(freq, np.abs(S))
plt.title("Magnitud de S")
plt.show()
#2
Ess = np.sum(s**2)
EsS = np.sum(np.abs(S)**2) / len(s)
print("Relación de energía (EsS/Ess):", EsS / Ess)

#Final
s_1 = np.sin(2 * np.pi * 10 * t) + 4*np.sin(2*np.pi * 20 * t) + 4
S_1 = fourier(s_1) #agrega frecuencia 0

s_2 = np.sin(2 * np.pi * 10 * t) + 4*np.sin(2*np.pi * 11 * t)
S_2 = fourier(s_2) #crea picos cercanos pero distinguibles

s_3 = np.sin(2 * np.pi * 10 * t) + 4*np.sin(2*np.pi * 10.5 * t)
S_3 = fourier(s_3) #genera superpocision de frecuencias

t2 = np.arange(0, 2, 1/fm)
s4 = np.sin(2*np.pi*10*t2) + 4*np.sin(2*np.pi*20*t2)
S4 = fourier(s4)
freq4 = frecuencias(1000, len(s4)) #mejora la precision del espectro

fig, ax = plt.subplots(2, 2, figsize=(12,8))
# S1
ax[0,0].stem(freq, np.abs(S_1))
ax[0,0].set_title('S1: Señal con offset')
ax[0,0].grid()
# S2
ax[0,1].stem(freq, np.abs(S_2))
ax[0,1].set_title('S2: Frecuencias 10Hz y 11Hz')
ax[0,1].grid()
# S3
ax[1,0].stem(freq, np.abs(S_3))
ax[1,0].set_title('S3: Frecuencias 10Hz y 10.5Hz')
ax[1,0].grid()
# S4
ax[1,1].stem(freq4, np.abs(S4))
ax[1,1].set_title('S4: Mayor duración temporal')
ax[1,1].grid()
plt.tight_layout()
plt.show()