import numpy as np
import matplotlib.pyplot as plt

# 1
def gen_random(fm, var=1):
    sigma = np.sqrt(var)  # Desviación estándar
    x = sigma * np.random.randn(fm) # Varianza ajustable por la desviación estándar
    return x

def senoidal(tini, tfin, fm, fs, fase=0, A=1):
    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = A*np.sin(2 * np.pi * fs * t + fase)
    return x

x = senoidal(0, 0.5, 1000, 100) + gen_random(500, var=0.5) #Se suma ruido a la señal senoidal

plt.plot(x)
plt.show()
x_norma2 = np.sqrt(np.sum(x**2))
x_energia = x_norma2**2
x_rms = x_norma2 / np.sqrt(len(x))
x_accion = np.sum(np.abs(x))
x_amplitud = np.max(np.abs(x))

# 2
y = senoidal(0, 0.5, 1000, 100)
parecido = np.dot(x, y) / (np.sqrt(np.sum(x**2)) * np.sqrt(np.sum(y**2))) #Similitud cosenoidal
angulo = np.arccos(parecido) * 180 / np.pi #hay un angulo de ~45°, es decir, las señales estan a medio camino entre ser ortogonales e iguales
print('Ángulo:', angulo)

# 3
phi1 = senoidal(0, 0.5, 1000, 100)
phi2 = senoidal(0, 0.5, 1000, 200)
parecido_phi1 = np.dot(x, phi1) / (np.sqrt(np.sum(x**2)) * np.sqrt(np.sum(phi1**2)))
parecido_phi2 = np.dot(x, phi2) / (np.sqrt(np.sum(x**2)) * np.sqrt(np.sum(phi2**2)))

x_aprox = parecido_phi1 * phi1 + parecido_phi2 * phi2
error = np.sqrt(np.sum((x - x_aprox)**2))
print('Error de aproximacion: ', error)
plt.plot(x, label='x')
plt.plot(x_aprox, label='x aproximada')
plt.legend()
plt.show()

# 4
y90 = senoidal(0, 0.5, 1000, 100, fase=np.pi/2)
parecido90 = np.dot(x, y90) / (np.sqrt(np.sum(x**2)) * np.sqrt(np.sum(y90**2))) #Similitud cosenoidal
angulo90 = np.arccos(parecido90) * 180 / np.pi #ahora hay un angulo de casi 90°, es decir, el cambio de fase hizo que las señales sean casi ortogonales
print('Parecido 90°:', parecido90) #lo que disminuyo mucho el grado de parecido