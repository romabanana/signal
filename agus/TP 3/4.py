import numpy as np
import matplotlib.pyplot as plt

# 1
t = np.linspace(-1,1,1000)
fs = np.arange(10) + 1
y = np.zeros((len(fs), len(t)))
for i in range(len(fs)):
    y[i] = np.sin(2 * np.pi * fs[i] * t)
x = np.sum(y, axis=0)

numerador = np.sum(x * y, axis=1)
denominador = np.sqrt(np.sum(x**2) * np.sum(y**2, axis=1)) #Similitud cosenoidal
parecido = numerador / denominador
plt.bar(fs, parecido) #Todas tienen el mismo parecido, porque x es una suma de senoides casi ortogonales entre si, que contribuyen igualmente
plt.xlabel('Frecuencia')
plt.ylabel('Similitud cosenoidal')
plt.grid()
plt.show()

# 2
y_fase = np.zeros((len(fs), len(t)))
#phi = (np.arange(len(fs))+1) * np.pi / 2
phi = np.random.rand(len(fs)) * np.pi / 2
for i in range(len(fs)):
    y_fase[i] = np.sin(2 * np.pi * fs[i] * t + phi[i])
x_fase = np.sum(y_fase, axis=0)

numerador = np.sum(x_fase * y, axis=1)
denominador = np.sqrt(np.sum(x_fase**2) * np.sum(y**2, axis=1)) #Similitud cosenoidal
parecido = numerador / denominador
plt.bar(fs, parecido) #Al variar la fase, las senoidales dejan de estar alineadas con x, entonces varia el parecido
plt.xlabel('Frecuencia')
plt.ylabel('Similitud cosenoidal')
plt.grid()
plt.show()

# 3
x_cuad = np.sign(np.sin(2 * np.pi * 5.5 * t))

numerador = np.sum(x_cuad * y, axis=1)
denominador = np.sqrt(np.sum(x_cuad**2) * np.sum(y**2, axis=1)) #Similitud cosenoidal
parecido = numerador / denominador
plt.bar(fs, parecido) #Como la frecuencia de 5.5Hz no esta representada en y, el parecido es bajo para todas las frecuencias
plt.xlabel('Frecuencia')
plt.ylabel('Similitud cosenoidal')
plt.grid()
plt.show()