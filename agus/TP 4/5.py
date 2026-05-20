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

t = np.arange(0, 1, 1/50)
s = 2 * np.sin(2*np.pi * 27 * t)

#creo el vector de frecuencias
fm = 50
N = len(s)
freq = frecuencias(fm, N)

S = fourier(s)

plt.stem(freq, np.abs(S))
plt.title("Espectro de la señal de 27Hz")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.show() #no se cumple la regla de fm > 2 * fs, entonces se ve una señal de 23Hz

#1
# Usando fk = k * fm / N, siendo fk la frecuencia observada, k el indice de la muestra, y N el numero de muestras
# fk = 23 * 50 / 50 = 23Hz, que es la frecuencia que se observa en la grafica, y no los 27Hz originales, debido al aliasing
# y por no cumplir el criterio de Nyquist

#2
# Señal usando Euler
n = np.arange(len(t))
s2 = (2/(2j)) * (
    np.exp(1j * 2*np.pi * 27 * n/fm)
    -
    np.exp(-1j * 2*np.pi * 27 * n/fm)
)

s2 = np.real(s2)# Parte real (equivale al seno)
S2 = fourier(s2)
plt.stem(n, np.abs(S2))
plt.title("Espectro de la señal con frecuencia 105Hz")
plt.xlabel("Muestras")
plt.ylabel("|x(k)|")
plt.show() #como no se cumple la regla de fm > 2 * fs, no se ven una grafica de 105Hz, sino una de 5Hz

#3
A = 2
s = A * np.sin(2*np.pi * 27 * t)
S = fourier(s) #magnitud de S con A = 1, 25
plt.figure()
plt.stem(t, s, 'b', label='señal original')
plt.figure()
plt.stem(freq, np.abs(S), 'r', label='señal transformada')
plt.title("Comparacion señal original y transformada")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.show() #la relacion entre amplitud de la señal original y el absoluto de su transformada es lineal,
# si aumenta la amplitud de la original, la magnitud de la transformada aumenta proporcionalmente
