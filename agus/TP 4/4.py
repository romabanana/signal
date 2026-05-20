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

t = np.arange(0, 1, 1/100)
s = np.sin(2*np.pi * 10 * t)
delta = np.zeros(len(t))
delta[50] = 1 #impulso en el centro

w1 = np.zeros(len(t))
w2 = np.zeros(len(t))
w3 = np.zeros(len(t))
# Ventanas

# Rectangular
w1 = np.where((t > 0.45) & (t < 0.55), 1, 0)  # muy angosta
w2 = np.where((t > 0.35) & (t < 0.65), 1, 0)  # media
w3 = np.where((t > 0.1) & (t < 0.9), 1, 0)    # ancha
"""
#Hanning
for n in range(len(t)):
    w1[n] = 0.5 * (1 - np.cos(2 * np.pi * n / (len(t) - 1))) if (t[n] > 0.45) & (t[n] < 0.55) else 0
    w2[n] = 0.5 * (1 - np.cos(2 * np.pi * n / (len(t) - 1))) if (t[n] > 0.35) & (t[n] < 0.65) else 0
    w3[n] = 0.5 * (1 - np.cos(2 * np.pi * n / (len(t) - 1))) if (t[n] > 0.1) & (t[n] < 0.9) else 0

#Blackman
for n in range(len(t)):
    w1[n] = 0.42 - 0.5 * np.cos(2 * np.pi * n / (len(t) - 1)) + 0.08 * np.cos(4 * np.pi * n / (len(t) - 1)) if (t[n] > 0.45) & (t[n] < 0.55) else 0
    w2[n] = 0.42 - 0.5 * np.cos(2 * np.pi * n / (len(t) - 1)) + 0.08 * np.cos(4 * np.pi * n / (len(t) - 1)) if (t[n] > 0.35) & (t[n] < 0.65) else 0
    w3[n] = 0.42 - 0.5 * np.cos(2 * np.pi * n / (len(t) - 1)) + 0.08 * np.cos(4 * np.pi * n / (len(t) - 1)) if (t[n] > 0.1) & (t[n] < 0.9) else 0
"""

x1 = s * w1
x2 = s * w2
x3 = s * w3
#x1 = delta * w1 #con dirac, la energia en el dominio temporal se concentra en un punto,
#x2 = delta * w2 #pero es constante a traves del dominio frecuencial
#x3 = delta * w3
X1 = fourier(x1)
X2 = fourier(x2)
X3 = fourier(x3)

freq = frecuencias(100, len(s))

fig, ax = plt.subplots(3,2, figsize=(12,8))
# Señales temporales
ax[0,0].plot(t,x1)
ax[0,0].set_title("Ventana angosta") #la señal dura poco, por lo que esta concentrada temporalmente, generando un espectro distribuido
ax[1,0].plot(t,x2)
ax[1,0].set_title("Ventana media")
ax[2,0].plot(t,x3)
ax[2,0].set_title("Ventana ancha") #como la ventana es mas ancha, hay mas informacion de la señal, por lo que el espectro se concentra en la frecuencia correcta, mejora la resolucion frecuencial
# Espectros
ax[0,1].stem(freq, np.abs(X1))
ax[0,1].set_title("Espectro angosto")
ax[1,1].stem(freq, np.abs(X2))
ax[1,1].set_title("Espectro medio")
ax[2,1].stem(freq, np.abs(X3))
ax[2,1].set_title("Espectro concentrado")
plt.tight_layout()
plt.show()

#concentrar una señal en el tiempo, implica dispersarla en la frecuencia