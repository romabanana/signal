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

def convolve(x, h):
    y = np.zeros((len(x) + len(h)) - 1)
    for i in range(len(y)):
        for j in range(len(x)):
            if i - j >= 0 and i - j < len(h):
                y[i] += x[j] * h[i - j]
    return y
def convolve_same(x, h):
    y = convolve(x, h)
    inicio = len(h)//2
    return y[inicio:inicio+len(x)]


fm = 12100
t = np.arange(0,1,1/1024)

N = 1024
freq = frecuencias(fm, N)
H = np.where(((np.abs(freq) >= 100) & (np.abs(freq) <= 200)) | ((np.abs(freq) >= 1640) & (np.abs(freq) <= 3028)) | ((np.abs(freq) >= 5000) & (np.abs(freq) <= 6000)), 1.0, 0.0)
idx = (np.abs(freq) >= 5000) & (np.abs(freq) <= 6000)
H[idx] = (np.abs(freq[idx]) - 5000)/1000
plt.plot(freq, H) 
plt.show()

# IDFT
h = np.zeros(len(H), dtype=complex)
for k in range(len(H)):
    for n in range(len(H)):
        h[k] += H[n]*np.exp(2j*np.pi*k*n/len(H))
h /= len(H)
h = h.real
N = len(h)
h = np.concatenate((h[N//2:], h[:N//2])) #para centrar el filtro en 0
plt.plot(h)
plt.show()

M = 51 #longitud del filtro
centro = len(h)//2
inicio = centro - M//2
fin = centro + M//2 + 1
#Rectangular
w = np.zeros(len(h))
w[inicio : fin] = 1

h_rect = h*w

#Hanning
wM = np.zeros(M)
for n in range(M):
    wM[n] = 0.5*(1 - np.cos(2*np.pi*n/(M-1)))
w = np.zeros(len(h))
w[inicio:fin] = wM

h_hanning = h * w

#Blackman
wM = np.zeros(M)
for n in range(M):
    wM[n] = (
        0.42
        - 0.5*np.cos(2*np.pi*n/(M-1))
        + 0.08*np.cos(4*np.pi*n/(M-1))
    )
w = np.zeros(len(h))
w[inicio:fin] = wM

h_blackman = h * w

H_rect = np.abs(fourier(h_rect))
H_hann = np.abs(fourier(h_hanning))
H_black = np.abs(fourier(h_blackman))

plt.plot(freq, H_rect, label="Rectangular")
plt.plot(freq, H_hann, label="Hanning")
plt.plot(freq, H_black, label="Blackman")
plt.legend()
plt.show()

signal = (
    np.sin(2*np.pi*150*t)    # pasa
    + np.sin(2*np.pi*1000*t) # debe eliminarse
    + np.sin(2*np.pi*4000*t) # debe eliminarse
    + np.sin(2*np.pi*5500*t) # pasa parcialmente
)
y = convolve_same(signal, h_rect)
plt.plot(t, signal, label="Original")
plt.plot(t, y, label="Filtrada")
plt.legend()
plt.show()