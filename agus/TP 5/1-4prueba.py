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

# H(s) = 12500 s / (44 s^2 + 60625 s + 6250000)

# Bilineal:
# H(z) = 12500 (2/T) [(1 - z^(-1)) / (1 + z^(-1))] / [44 (2/T)^2 [(1 - z^(-1)) / (1 + z^(-1))]^2 + 60625 (2/T) [(1 - z^(-1)) / (1 + z^(-1))] + 6250000]

# Euler:
# H(z) = 12500 (1/T) (1 - z^(-1)) / [44 (1/T)^2 (1 - z^(-1))^2 + 60625 (1/T) (1 - z^(-1)) + 6250000]

#1
# H(jw) = 12500 j w / (44 (j w)^2 + 60625 j w + 6250000)


freq = np.linspace(0, 5000, 5000)
H1 = 12500 * 1j * freq / (44 * (1j * freq)**2 + 60625 * 1j * freq + 6250000)

mag = np.abs(H1)
# máximo
Hmax = np.max(mag)
# nivel -3 dB
nivel_3db = Hmax / np.sqrt(2) # 20*log10(1/sqrt(2)) = - 3dB
# índice más cercano
idx = np.argmin(np.abs(mag - nivel_3db))
fc = freq[idx] #/ (2 * np.pi) # convertir a Hz

print("Frecuencia de corte (-3dB):", fc, "rad/s")

T = 1 / (4 * fc) # frecuencia de muestreo 4 veces la frecuencia de corte
w = freq / 6 * 2 * np.pi
z = np.exp(1j*w*T)
# Euler
s_euler = (1 - z**(-1)) / T
# Bilineal
s_bili = (2/T)*(1 - z**(-1))/(1 + z**(-1))
# H(z)
He = 12500*s_euler / (
    44*s_euler**2 +
    60625*s_euler +
    6250000
)
Hb = 12500*s_bili / (
    44*s_bili**2 +
    60625*s_bili +
    6250000
)
# gráficos
plt.plot(freq, np.abs(H1), label='Continuo')
plt.plot(w, np.abs(He), label='Euler')
plt.plot(w, np.abs(Hb), label='Bilineal')

plt.xlabel("Frecuencia rad/s")
plt.ylabel("Magnitud")
plt.title("Comparación de discretizaciones")

plt.grid(True)
plt.legend()
plt.show()