import numpy as np
import matplotlib.pyplot as plt

# 1
t = np.linspace(-1,1,1000)
# Señal original
y = np.where(t < 0, -1, 1)
# Aproximación del libro
a1 = np.sqrt(3/2)
a3 = -np.sqrt(7/32)
phi1 = (np.sqrt(3/2)*t)
phi3 = (np.sqrt(7/2)*((5/2)*t**3 - (3/2)*t))
y_aprox = a1*phi1 + a3*phi3
# Error cuadrático total
E = np.sum((y - y_aprox)**2)
print("Error cuadrático:", E)

plt.plot(t,y,label='Original')
plt.plot(t,y_aprox,label='Aprox')
plt.legend()
plt.grid()
plt.show()

# 2
a1_var = np.linspace(a1 - 1,
                      a1 + 1,
                      50)
a3_var = np.linspace(a3 - 1,
                      a3 + 1,
                      50)
A1, A3 = np.meshgrid(a1_var, a3_var)
E = np.zeros_like(A1)

x_eje = []
y_eje = []
z_eje = []


for i in range(len(a1_var)):
    for j in range(len(a3_var)):

        y_aprox = a1_var[i]*phi1 + a3_var[j]*phi3
        error = np.sum((y - y_aprox)**2)

        x_eje.append(a1_var[i])
        y_eje.append(a3_var[j])
        z_eje.append(error)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_eje, y_eje, z_eje)
ax.set_xlabel('a1')
ax.set_ylabel('a3')
ax.set_zlabel('Error')
plt.show()

# 3
"""
from numpy.polynomial.legendre import legfit, legval
errores = []
grados = range(1,21)
for M in grados:
    # Calcula coeficientes de Legendre hasta grado M
    coeffs = legfit(t, y, M)
    # Reconstrucción
    y_aprox = legval(t, coeffs)
    # Error cuadrático
    E = np.sum((y - y_aprox)**2)
    errores.append(E)
plt.plot(grados, errores)
plt.xlabel('Cantidad de coeficientes')
plt.ylabel('Error cuadrático')
plt.grid()
plt.show()
"""
import math
from scipy.special import eval_legendre
def legendre(n, t):
    P = (t**2 - 1)**n
    dt = t[1] - t[0]
    for _ in range(n):
        P = np.gradient(P, dt) #Esto se vuelve inestable a partir de n>11
    P = P / (2**n * math.factorial(n))
    return P
def phi(n, t):
    Pn = legendre(n, t)
    #Pn = eval_legendre(n, t) #Esto mantiene estabilidad
    return np.sqrt((2*n + 1)/2) * Pn
def integral(x, t):
    return np.trapezoid(x, t)

Nmax = 11 #Explota a partir de 11, porque el calculo recurrente de gradientes se vuelve cada vez mas inestable
error = np.zeros(Nmax)
y_legendre = np.zeros_like(t)

for n in range(Nmax):
    phi_n = phi(n, t)
    alpha_n = integral(phi_n * y, t)
    y_legendre += alpha_n * phi_n

    error[n] = np.sum((y - y_legendre)**2)

plt.plot(range(Nmax), error)
plt.xlabel('Cantidad de coeficientes')
plt.ylabel('Error cuadrático')
plt.grid()
plt.show()