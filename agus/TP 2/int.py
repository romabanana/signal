import numpy as np
import matplotlib.pyplot as plt

# y[n] - 0.6*y[n-1] = x[n] + 0.2*x[n-1]
# y[n] = x[n] + 0.2*x[n-1] + 0.6*y[n-1]

#///////////////////Parte 1////////////////////////////#

#Lineal, puede representarse como una conbinacion lineal.
#Invariante en el tiempo, los coeficientes que acompañan a las variantes
#son constantes.
#Causal, no requiere el uso de entradas futuras.
#IIR, porque h no se anula, solo tiende a 0 (ver h)


#///////////////////Parte 2////////////////////////////#

N = 20
delta = np.zeros(N)
delta[0] = 1  # Impulso unitario
h = np.zeros(len(delta))
for n in range(len(delta)):
    if n >= 1:
        h[n] = delta[n] + 0.2*delta[n-1] + 0.6*h[n-1]
    else:
        h[n] = delta[n]

plt.stem(h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.show()

#El sistema es estable porque tiende a 0


#///////////////////Parte 3////////////////////////////#
L = 10
x = np.random.rand(L)

ya = np.zeros(L + N - 1)
for i in range(len(ya)):
    for j in range(len(x)):
        if i - j >= 0 and i - j < len(h):
            ya[i] += x[j] * h[i - j]

H = np.zeros((L, L))
yb = np.zeros(L)
for i in range(L):
    for j in range(i + 1):
        if i - j >= 0 and i - j < len(h):
            H[i, j] = h[i - j]
for i in range(len(x)):
    yb[i] = np.dot(H[i, :], x) #no toma en cuenta el caso en el que i >= len(h)

N_total = L + len(h) - 1
x_pad = np.concatenate([x, np.zeros(len(h)-1)])
h_pad = np.concatenate([h, np.zeros(L-1)])
yc = np.zeros(N_total)
for k in range(N_total):
    for l in range(N_total):
        yc[k] += h_pad[l] * x_pad[(k - l) % N_total]

print('\ny sumatoria: ', ya[:10])
print('y matricial: ', yb)
print('y circularr: ', yc[:10])
#Las 3 son iguales


#///////////////////Parte 4////////////////////////////#

x_desconv = np.zeros(L)
xr_desconv = np.zeros(L)
ruido = 0.5 * np.random.rand(len(ya))
yar = ya + ruido
for n in range(L):
    if n >= 1:
        x_desconv[n] = ya[n] - 0.6*ya[n-1] - 0.2*x_desconv[n-1]
        xr_desconv[n] = yar[n] - 0.6*yar[n-1] - 0.2*xr_desconv[n-1]
    else:
        x_desconv[n] = ya[n]
        xr_desconv[n] = yar[n]

print('\nx[n] = ', x)
print('x_desconv[n] = ', x_desconv)
print('xr_desconv[n] = ', xr_desconv)

#Se recupera una señal incorrecta, el sistema inverso amplifica el ruido
#porque lo "desfiltra", contrario al filtrado del sistema directo