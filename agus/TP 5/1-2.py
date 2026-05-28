import numpy as np
import matplotlib.pyplot as plt

def frecuencias(fm, N):
    freq = np.zeros(N)
    for k in range(N):
        if k < N//2:
            freq[k] = k * fm / N
        else:
            freq[k] = (k - N) * fm / N #para representar la simetria de frecuencias
    return freq

fm = 10000
freq = frecuencias(fm, 100)
freq = 2 * np.pi * freq / fm #frecuencia angular

#1. H(z) = 1 / [1 - 1/2 z^(-1) + 1/5 z^(-2)]
#   H(e^(jw)) = 1 / [1 - 1/2 e^(-jw) + 1/5 e^(-jw2)]
H1 = 1 / (1 - 0.5 * np.exp(-1j * freq) + 0.2 * np.exp(-2j * freq))
plt.plot(freq, np.abs(H1))
plt.title("Sistema 1")
plt.xlabel("Frecuencia (radianes/muestra)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()

#2. H(z) = z^(-1) / [1 - z^(-1) - z^(-2)]
#   H(e^(jw)) = e^(-jw) / [1 - e^(-jw) - e^(-jw2)]
H2 = np.exp(-1j * freq) / (1 - np.exp(-1j * freq) - np.exp(-2j * freq))
plt.plot(freq, np.abs(H2))
plt.title("Sistema 2")
plt.xlabel("Frecuencia (radianes/muestra)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()

#3. H(z) = 7 / [1 - 2 z^(-1) + 6 z^(-2)]
#   H(e^(jw)) = 7 / [1 - 2 e^(-jw) + 6 e^(-jw2)]
H3 = 7 / (1 - 2 * np.exp(-1j * freq) + 6 * np.exp(-2j * freq))
plt.plot(freq, np.abs(H3))
plt.title("Sistema 3")
plt.xlabel("Frecuencia (radianes/muestra)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()

#4. H(z) = sum(k=0... 7) [2^(-k) z^(-k)]
#   H(e^(jw)) = sum(k=0... 7) [2^(-k) e^(-jwk)]
H4 = np.sum([2**(-k) * np.exp(-1j * k * freq) for k in range(8)], axis=0)
plt.plot(freq, np.abs(H4))
plt.title("Sistema 4")
plt.xlabel("Frecuencia (radianes/muestra)")
plt.ylabel("Magnitud") # el grafico muestra que,
plt.grid(True)# la muestra actual pesa más,
plt.show() # las anteriores pesan progresivamente menos. 
#Sino se puede decir que se asentuan las frecuencias cercanas a 0 radianes/muestra y se atenuan las mayores a |1.3~|
