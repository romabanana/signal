import numpy as np
import matplotlib.pyplot as plt

def gen_random(r, fm):
    x = np.random.randn(r, fm)

    return x

r = [10, 50, 200, 500, 1000, 2000]
med = np.zeros(len(r))
var = np.zeros(len(r))

for i in range(len(r)):
    t, x = gen_random(r[i], 5)
    med[i] = np.mean(x)
    var[i] = np.var(x)

plt.grid(True)
plt.plot(r, med, label='Media')
plt.plot(r, var, label='Varianza')
plt.show()