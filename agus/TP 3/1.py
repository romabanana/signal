import numpy as np
import matplotlib.pyplot as plt

N = 100
n = np.arange(N)

# Señal senoidal
fs = 0.05  # Frecuencia de la señal
x_sin = np.sin(2 * np.pi * fs * n)

# Señal rampa
a = 1 #Pendiente
x_rampa = a*n

# Señal cuadrada
fsc = 0.05  # Frecuencia de la señal cuadrada
x_cuad = np.sign(np.sin(2 * np.pi * fsc * n))

# Señal aleatoria
x_rand = np.random.randn(N)

#Valor Medio
sin_valor_medio = np.mean(x_sin)
rampa_valor_medio = np.mean(x_rampa)
cuad_valor_medio = np.mean(x_cuad)
rand_valor_medio = np.mean(x_rand)
#Maximo
sin_maximo = np.max(x_sin)
rampa_maximo = np.max(x_rampa)
cuad_maximo = np.max(x_cuad)
rand_maximo = np.max(x_rand)
#Minimo
sin_minimo = np.min(x_sin)
rampa_minimo = np.min(x_rampa)
cuad_minimo = np.min(x_cuad)
rand_minimo = np.min(x_rand)
#Amplitud
sin_amp = np.max(np.abs(x_sin))
rampa_amp = np.max(np.abs(x_rampa))
cuad_amp = np.max(np.abs(x_cuad))
rand_amp = np.max(np.abs(x_rand))
#Energia
sin_ener = np.sum(x_sin**2)
rampa_ener = np.sum(x_rampa**2)
cuad_ener = np.sum(x_cuad**2)
rand_ener = np.sum(x_rand**2)
#Accion
sin_accion = np.sum(np.abs(x_sin))
rampa_accion = np.sum(np.abs(x_rampa))
cuad_accion = np.sum(np.abs(x_cuad))
rand_accion = np.sum(np.abs(x_rand))
#Potencia Media
sin_potencia = np.mean(x_sin**2)
rampa_potencia = np.mean(x_rampa**2)
cuad_potencia = np.mean(x_cuad**2)
rand_potencia = np.mean(x_rand**2)
#RMS
sin_rms = np.sqrt(sin_potencia)
rampa_rms = np.sqrt(rampa_potencia)
cuad_rms = np.sqrt(cuad_potencia)
rand_rms = np.sqrt(rand_potencia)

"""
print("Valor Medio: ", elvalorquequiera)
plt.plot(n, loquequiera)
plt.show()
"""