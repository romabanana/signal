import numpy as np
import matplotlib.pyplot as plt

#1

# H(z) = [1 - 2 z^(-1) + 2 z^(-2) - z^(-3)] / {[1 - z^(-1)][1 - 0.5 z^(-1)][1 - 0.2 z^(-1)]}
# H(z) = [1 - 2 z^(-1) + 2 z^(-2) - z^(-3)] / [1 − 1.7 z^(-1) + 0.8 z^(-2) − 0.1 z^(-3)]

a = np.array([1, -2, 2, -1])
b = np.array([1, -1.7, 0.8, -0.1])
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
plt.title('Diagrama de polos y ceros')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

#2

# H(z) = [1 - 2 z^(-1) + 2 z^(-2) - z^(-3)] / {[1 - z^(-1)][1 - 0.5 z^(-1)][1 - 0.2 z^(-1)]}

# H(z) = [1 - 2 z^(-1) + 2 z^(-2) - z^(-3)] / [1 − 1.7 z^(-1) + 0.8 z^(-2) − 0.1 z^(-3)] = Y(z) / X(z)
# y[n] − 1.7 y[n−1] + 0.8 y[n−2] − 0.1 y[n−3] = x[n] − 2 x[n−1] + 2 x[n−2] − x[n−3]
# y[n]=  1.7y[n−1] − 0.8y[n−2] + 0.1y[n−3] + x[n]−2x[n−1]+2x[n−2]−x[n−3]

# Y(z) {[1 - z^(-1)][1 - 0.5 z^(-1)][1 - 0.2 z^(-1)]} = X(z) [1 - 2 z^(-1) + 2 z^(-2) - z^(-3)]
# {(y[n] - y[n-1])(y[n] - 0.5 y[n-1])(y[n] - 0.2 y[n-1])} = x[n] - 2 x[n-1] + 2 x[n-2] - x[n-3]
# y[n] (1 - y[n-1])(1 - 0.5 y[n-1])(1 - 0.2 y[n-1]) = x[n] - 2 x[n-1] + 2 x[n-2] - x[n-3]
# y[n]  = (x[n] - 2 x[n-1] + 2 x[n-2] - x[n-3] ) / {(1 - y[n-1])(1 - 0.5 y[n-1])(1 - 0.2 y[n-1])}

delta = np.zeros(100)
delta[0] = 1  # impulso unitario
h = np.zeros(len(delta))
for n in range(len(delta)):
    # entradas
    x0 = delta[n]
    x1 = delta[n-1] if n >= 1 else 0
    x2 = delta[n-2] if n >= 2 else 0
    x3 = delta[n-3] if n >= 3 else 0
    # salidas previas
    y1 = h[n-1] if n >= 1 else 0
    y2 = h[n-2] if n >= 2 else 0
    y3 = h[n-3] if n >= 3 else 0
    # ecuación en diferencias
    h[n] = (
        1.7*y1
        -0.8*y2
        +0.1*y3
        +x0
        -2*x1
        +2*x2
        -x3
    )
plt.stem(h)
plt.title("Respuesta al impulso")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)
plt.show()