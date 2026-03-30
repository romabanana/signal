import numpy as np
import matplotlib.pyplot as plt

def senoidal(tini, tfin, fm, fs, fase=0, A=1):

    T = 1 / fm
    t = np.arange(tini, tfin, T)
    x = A*np.sin(2 * np.pi * fs * t + fase)

    return t, x

def cuantizar(x, N=8):
    #N = número de niveles
    H = (np.max(x)-np.min(x)) / N #magnitud del cuanto basada en el rango de la señal

    x_alter = x - np.min(x) #desplaza la señal para que el mínimo sea 0
    x_cu = np.where(x_alter >= (N-1)*H, (N-1)*H, np.round(x_alter / H) * H) #cuantiza la señal
    x_cu = x_cu + np.min(x) #desplaza la señal de vuelta a su rango original

    return x_cu

#///////PARTE 1///////#
t, x = senoidal(0, 1, 400, 10, np.pi/4, 5)

#Clasificacion
# Fenomenologica: Deterministica, periodica sinusoidal
# Morfologica: Discreta Muestreada

x_rec = np.abs(x) #rectificada
x_cu = cuantizar(x_rec, N=16) #cuantizada

# Graficas
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.stem(t, x, 'b-', label='Señal original x')
plt.title('Stem de x')
plt.xlabel('t')
plt.ylabel('x')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.stem(t, x_cu, 'r-', label='Señal cuantizada x_cu')
plt.title('Stem de x_cu')
plt.xlabel('t')
plt.ylabel('x_cu')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

#Disminuyo ligeramente la amplitud en la señal cuantizada por cuestiones de redondeo o precision

#///////PARTE 2///////#
def gen_random(fm, var=1):
    sigma = np.sqrt(var)  # Desviación estándar
    x = sigma * np.random.randn(fm)
    return x

def potency(x):
    return np.mean(x**2)

# Generar dos ruidos con varianzas diferentes
r1 = gen_random(fm=400, var=1)
r2 = gen_random(fm=400, var=2)

# Señales ruidosas
xr1 = x + r1
xr2 = x + r2

# Graficas
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
plt.stem(t, x, 'b-', label='Señal original')
plt.title('Señal Original')
plt.xlabel('t')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 2)
plt.stem(t, xr1, 'r-', label='Señal con ruido 1')
plt.title('Señal con Ruido 1')
plt.xlabel('t')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 3)
plt.stem(t, xr2, 'g-', label='Señal con ruido 2')
plt.title('Señal con Ruido 2')
plt.xlabel('t')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

Px = potency(x)
Pr1 = potency(r1)
Pr2 = potency(r2)

print(f"\nPotencia de la señal original: {Px:.4f}")
print(f"Potencia del ruido 1: {Pr1:.4f}")
print(f"Potencia del ruido 2: {Pr2:.4f}")

"""""
snr(db) = 10 * log(Ps / Par) -> Da 6 si log EX = 0.6, entonces EX = 10^(6/10) = 3.98 aprox = Ps / Pr
|
|
V
Par = 1/N * E (k*r)^2 -> r es el ruido, k es el factor de amplificación. E es la sumatoria, Par es la potencia del ruido amplificado. N es el número de muestras.
Par = 1/N * E (k)^2 * (r)^2 -> k es constante, entonces:
Par = k^2 * (1/N * E r^2) = k^2 * Pr

Ps / Par = 3.98
Ps / (k^2 * Pr) = 3.98
k^2 = Ps / (3.98 * Pr)
k = sqrt(Ps / (3.98 * Pr))
"""""

k1 = np.sqrt(Px / (3.98 * Pr1))
k2 = np.sqrt(Px / (3.98 * Pr2))

rk1 = k1 * r1
rk2 = k2 * r2
Prk1 = potency(rk1)
Prk2 = potency(rk2)

SNRk1 = 10 * np.log10(Px / Prk1)
SNRk2 = 10 * np.log10(Px / Prk2)

print(f"\nFactor de amplificación para ruido 1: {k1:.4f}")
print(f"Potencia del ruido amplificado 1: {Prk1:.4f}")
print(f"Relación señal a ruido con ruido amplificado 1 (SNR_k1): {SNRk1:.2f} dB")
print(f"Factor de amplificación para ruido 2: {k2:.4f}")
print(f"Potencia del ruido amplificado 2: {Prk2:.4f}")
print(f"Relación señal a ruido con ruido amplificado 2 (SNR_k2): {SNRk2:.2f} dB")

#/////////PARTE 3///////#
# Al disminuir los niveles de cuatizacion, baja la fiabilidad porque hay menos escalones que representen a la señal,
# ademas la amplitud disminuye incluso mas

# Con menor frecuencia de muestreo, otra vez se pierde informacion, la señal se vuelve mas escalonada y discreta, al punto
# en el que se puede perder la amplitud maxima

# Para obtener una SNR de 0 db, se aplica la formula como se vio en el ejercicio 8 