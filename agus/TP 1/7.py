import numpy as np
import matplotlib.pyplot as plt

def gen_random(r, fm):
    x = np.random.randn(r, fm)

    return x

r = [10, 50, 200, 500, 1000, 2000, 5000]
med = np.zeros(len(r))
var = np.zeros(len(r))

#Ergodicidad
for i in range(len(r)):
    x = np.random.randn(r[i])
    med[i] = np.mean(x)
    var[i] = np.var(x)
print(np.mean(med), np.mean(var))

plt.grid(True)
plt.plot(r, med, label='Media')
plt.plot(r, var, label='Varianza')
plt.legend()
plt.show()

#Estacionariedad
med = []
var = []
for i in range(len(r)):
    med_aux, var_aux = [], []
    x = np.random.randn(r[i], r[i])
    t_indices = np.arange(0, r[i], 1)
    for t in t_indices:
        med_aux.append(np.mean(x[:, t]))
        var_aux.append(np.var(x[:, t]))
    med.append(np.mean(med_aux))
    var.append(np.mean(var_aux))

plt.grid(True)
plt.plot(r, med, label='Media')
plt.plot(r, var, label='Varianza')
plt.legend()
plt.show()