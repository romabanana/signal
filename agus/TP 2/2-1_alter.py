import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 2])
h = np.array([2, 1, 0.5])
y = np.zeros((len(x) + len(h)) - 1)

N = len(h)
H = np.zeros((N, N))

for i in range(N):
    for j in range(i + 1):
        if i - j >= 0 and i - j < len(h):
            H[i, j] = h[i - j]

for i in range(len(x)):
    y[i] = np.dot(H[i, :], x) #no toma en cuenta el caso en el que i >= len(h)

plt.stem(y)
plt.title('Convolution of x and h')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.show()
