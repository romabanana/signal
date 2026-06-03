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

#Parte 1

# y[n] - 0.8 t[n-1] + 0.12 y[n-2] = x[n] + 0.5 x[n-1]
# Y(z) - 0.8 Y(z) z^(-1) + 0.12 Y(z) z^(-2) = X(z) + 0.5 X(z) z^(-1)
# H(z) = Y(z) / X(z) = (1 + 0.5 z^(-1)) / (1 - 0.8 z^(-1) + 0.12 z^(-2))

a = np.array([1, 0.5, 0]) # añado un 0 para que el numerador tenga el mismo orden que el denominador
b = np.array([1, -0.8, 0.12])
ceros = np.roots(a)
polos = np.roots(b)
print("Ceros: ", ceros)
print("Polos: ", polos)

# círculo unitario
theta = np.linspace(0, 2*np.pi, 500)
x = np.cos(theta)
y = np.sin(theta)
plt.figure(figsize=(6,6))
plt.plot(x, y, 'k--', label='Círculo unitario')
# ejes
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
# ceros
plt.scatter(
    np.real(ceros),
    np.imag(ceros),
    marker='o',
    s=100,
    facecolors='none',
    edgecolors='blue',
    label='Ceros'
)
# polos
plt.scatter( # todos los polos estan dentro del circulo unitario, por lo tanto el sistema es estable
    np.real(polos),
    np.imag(polos),
    marker='x',
    s=100,
    color='red',
    label='Polos'
)
plt.xlabel('Parte real')
plt.ylabel('Parte imaginaria')
plt.title('Diagrama de polos y ceros - Parte 1')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

#Parte 2
fm = 1000
N = 512
freq = frecuencias(fm, N)

# H(z) = Y(z) / X(z) = (1 + 0.5 z^(-1)) / (1 - 0.8 z^(-1) + 0.12 z^(-2))
z = np.exp(1j * 2 * np.pi * freq / fm)
H = (1 + 0.5 * z**(-1)) / (1 - 0.8 * z**(-1) + 0.12 * z**(-2))
plt.plot(freq/fm, np.abs(H))
plt.title("Respuesta en frecuencia - Parte 2")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.show() # se asemeja a un filtro pasa bajos, siendo el pico mas alto en 0Hz y atenudo en las frecuencias mas altas

plt.plot(freq, np.unwrap(np.angle(H))) # obtengo la fase sin saltos de 2pi calculando el angulo entre numerador y denominador de H(z)
plt.title("Fase - Parte 2")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (rad)")
plt.grid(True)
plt.show()

delta = np.zeros(50)
delta[0] = 1
h = np.zeros(50)
for n in range(50):
    x0 = delta[n]
    x1 = delta[n-1] if n>=1 else 0

    y1 = h[n-1] if n>=1 else 0
    y2 = h[n-2] if n>=2 else 0

    h[n] = (
        x0
        + 0.5*x1
        + 0.8*y1
        - 0.12*y2
    )
plt.plot(h)
plt.title("Respuesta al impulso - Parte 2")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show() # es estable porque tiende a 0

#Parte 3

# H(s) = 1 / (s + 1)
T = 0.1

s_euler = (1-z**(-1))/T
H_euler = 1 / (s_euler + 1) # Hs = 1 / ((1 - z^(-1))/T + 1)) = T / (1 - z^(-1) + T)

s_jw = 1j * 2 * np.pi * freq
H_jw = 1 / (s_jw + 1) # Hs = 1 / (jw + 1)

plt.plot(freq, np.abs(H_euler), label="Euler")
plt.plot(freq, np.abs(H_jw), label="Analítica")
plt.title("Comparación de métodos de discretización - Parte 3")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.show()

#Parte 4

s_bili = (2/T) * (1-z**(-1))/(1+z**(-1))
H_bili = 1 / (s_bili + 1) # Hs = 1 / ((2/T) * (1-z^(-1))/(1+z^(-1)) + 1))

plt.plot(freq, np.abs(H_bili), label="Bilinear")
plt.plot(freq, np.abs(H_euler), label="Euler")
plt.plot(freq, np.abs(H_jw), label="Analítica")
plt.title("Comparación de métodos de discretización - Parte 4")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.show() # bilineal muestra una mejor aproximacion a la analitica, pero requiere mas calculos