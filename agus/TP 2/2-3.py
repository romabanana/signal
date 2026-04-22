import numpy as np
import matplotlib.pyplot as plt

def circle_convolve(x, h):
    N = len(h)
    y = np.zeros(N)
    for k in range(N):
        for l in range(N):
            y[k] += h[l] * x[(np.mod((N + k - l), N))]
    return y

def convolve(x, h):
    y = np.zeros((len(x) + len(h)) - 1)
    for i in range(len(y)):
        for j in range(len(x)):
            if i - j >= 0 and i - j < len(h):
                y[i] += x[j] * h[i - j]
    return y

N = 4
a = 0.5

hA = np.zeros(N)
hB = np.zeros(N)

for n in range(N):
    hA[n] = np.sin(8 * n)
    hB[n] = np.pow(a,n)

delta = np.zeros(N)
delta[0] = 1
x = np.zeros(N)
for n in range(N):
    if n - 1 >= 0:
        x[n] = delta[n] - a * delta[n-1]
    else:
        x[n] = delta[n]
#x = [1, -0.5, 0, 0]

#y = np.zeros(N)
w = convolve(x, hA)
y = convolve(w, hB)
print("y[n] = ", y[:N])

w = convolve(x, hB)
yr = convolve(w, hA)
print("y[n] reversa = ", yr[:N])
print(np.allclose(y[:N], yr[:N]))