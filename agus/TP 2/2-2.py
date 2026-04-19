import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 2, 0])
h = np.array([2, 1, 0.5, 0])
N = len(h)

y = np.zeros(N)

for k in range(N):
    for l in range(N):
        y[k] += h[l] * x[(np.mod((N + k - l), N))]

plt.stem(y)
plt.title('Circular Convolution of x and h')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.show()