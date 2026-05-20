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

#Parte 1
fm = 1000
t = np.arange(0, 1, 1/fm)
s1 = 5 * np.sin(2*np.pi * 50 * t)
s2 = 3 * np.sin(2*np.pi * 120 * t)
s3 = 2 * np.sin(2*np.pi * 280 * t)
s = s1 + s2 + s3
plt.plot(t, s)
plt.title("Señal Original")
plt.show()

S = fourier(s)
freq = frecuencias(fm, len(s))
plt.stem(freq, np.abs(S))
plt.title("Espectro de Frecuencias TDF")
plt.show()
deltaFm = fm / len(s)
print("Resolucion frecuencial: ", deltaFm)

fm = 200
t = np.arange(0, 1, 1/fm)
s1 = 5 * np.sin(2*np.pi * 50 * t)
s2 = 3 * np.sin(2*np.pi * 120 * t)
s3 = 2 * np.sin(2*np.pi * 280 * t)
s = s1 + s2 + s3
S = fourier(s)
freq = frecuencias(fm, len(s))
plt.stem(freq, np.abs(S))
plt.title("Espectro de Frecuencias TDF en 200Hz")
plt.show() #solo se observa la frecuencia de 50Hz de las originales, porque esta dentro del rango que cumple el criterio de fm > 2*fs
#mientras que se obserba una frecuencia de 80Hz para las componentes de 120Hz y 280Hz
#|a*fm - fs| = frecuencia_observada_con_aliasing
#|200 - 120| = |280 - 200| = 80

#Parte 2
fm = 1000
t = np.arange(0, 0.04, 1/fm) #40ms
s1 = 5 * np.sin(2*np.pi * 50 * t)
s2 = 3 * np.sin(2*np.pi * 120 * t)
s3 = 2 * np.sin(2*np.pi * 280 * t)
s = s1 + s2 + s3
S = fourier(s)
freq = frecuencias(fm, len(s))
plt.stem(freq, np.abs(S))
plt.title("Espectro de Frecuencias TDF en 40ms")
plt.show() #Solo se distingue el pico de 50Hz, luego otro en 124Hz y otro en 276Hz, pero no se distinguen claramente las frecuencias de 120Hz y 280Hz, debido a la baja resolucion espectral causada por el corto tiempo de observacion de la señal
deltaFm = fm / len(s)
print("Resolucion frecuencial con 40ms: ", deltaFm)

s_ext = np.zeros(len(s)*5)
s_ext[:len(s)] = s
S_ext = fourier(s_ext)
freq_ext = frecuencias(fm, len(s_ext))
plt.stem(freq, np.abs(S), 'blue', label='Señal N')
idx = np.argsort(freq_ext) #para ordenar las frecuencias y evitar deformidades visuales
plt.plot(freq_ext[idx], np.abs(S_ext)[idx], 'r') #los "picos" son anchos, demostrando que no mejoro la resolucion espectral
plt.title("Espectro de Frecuencias TDF en con señal 5N")
plt.legend()
plt.show() #no mejora la resolucion frecuencial, pero hace mas detallada la vista del espectro
#mejorar la resolucion espectral implica observar la señal por mas tiempo para reducir la resolucion frecuencias y poder distinguir mas frecuencias,
#mejorar la visualizacion implica aumentar los detalles del espectro visible

#Parte 3
fm = 1000
t = np.arange(0, 1, 1/fm)
s1 = 5 * np.sin(2*np.pi * 50 * t)
s2 = 3 * np.cos(2*np.pi * 120 * t)
s3 = 2 * np.sin(2*np.pi * 280 * t)
s = s1 + s2 + s3
S = fourier(s)
S1 = fourier(s1)
S2 = fourier(s2)
S3 = fourier(s3)
freq = frecuencias(fm, len(s))
# Graficos
fig, ax = plt.subplots(2,2, figsize=(12,8))
ax[0,0].stem(freq, np.abs(S1))
ax[0,0].set_title("Magnitud |S1|")
ax[0,1].stem(freq, np.abs(S2))
ax[0,1].set_title("Magnitud |S2|")
ax[1,0].stem(freq, np.abs(S3))
ax[1,0].set_title("Magnitud |S3|")
ax[1,1].stem(freq, np.abs(S), linefmt='b-', markerfmt='bo', basefmt=' ', label='|S|')
ax[1,1].set_title("Original")
ax[1,1].legend()
plt.tight_layout()
plt.show()

S_sum = S1 + S2 + S3
plt.figure(figsize=(10,5))
plt.stem(freq, np.abs(S), 'b', label='|S| original')
plt.stem(freq, np.abs(S_sum), 'r', label='|S1+S2+S3|')
plt.title("Verificación de linealidad de la TDF")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.show() #se verifica linealidad

s_energia = np.sum(np.abs(s)**2)
S_energia = np.sum(np.abs(S)**2) / len(s)
print("Energia de s: ", s_energia)
print("Energia de S: ", S_energia) #son equivalentes

#Parte 4
H = np.where(np.abs(freq) < 200, 1, 0)
plt.stem(freq, H)
plt.title("Respuesta en frecuencia del filtro")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("H[k]")
plt.show()

S_filtered = S * H
plt.stem(freq, np.abs(S_filtered))
plt.title("Señal filtrada a 200Hz")
plt.show()

s_inv = np.zeros(len(s), dtype=complex)
for k in range(len(s)):
    for n in range(len(s)):
        s_inv[k] += S_filtered[n] * np.exp(2j * np.pi * k * n / len(s))
s_inv /= len(s)
#t1 = np.where(t<0.11, t, 0)
idx = t < 0.11 #mascara booleana
plt.plot(t[idx], s[idx], label='Original')
plt.plot(t[idx], s_inv.real[idx], label='Filtrada')
plt.title("Comparacion Original - Filtrada")
plt.legend()
plt.show() #la señal filtrada se ve distinta debido a que ya no cuenta con la suma de las frecuencias mayores a 200Hz
