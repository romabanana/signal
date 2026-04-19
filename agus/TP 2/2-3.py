import numpy as np
import matplotlib.pyplot as plt

def circle_convolve(x, h):
    N = len(h)
    y = np.zeros(N)
    for k in range(N):
        for l in range(N):
            y[k] += h[l] * x[(np.mod((N + k - l), N))]
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
w = circle_convolve(x, hA)
y = circle_convolve(w, hB)
print("y[n] = ", y)

w = circle_convolve(x, hB)
yr = circle_convolve(w, hA)
print("y[n] reversa = ", yr)