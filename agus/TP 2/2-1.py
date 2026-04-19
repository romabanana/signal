import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 2])
h = np.array([2, 1, 0.5])
y = np.zeros((len(x) + len(h)) - 1)

for i in range(len(y)):
    for j in range(len(x)):
        if i - j >= 0 and i - j < len(h):
            y[i] += x[j] * h[i - j]

plt.stem(y)
plt.title('Convolution of x and h')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.show()


from scipy.signal import lfilter

print("Convolution result:", y)
y_straight = np.convolve(x, h)
print("Convolution result using np.convolve:", y_straight)
x_padded = np.concatenate([x, np.zeros(len(h)-1)])
y_filter = lfilter(h,[1],x_padded)
print("Convolution result using lfilter:", y_filter)

#B y A corresponden a los coeficientes de entrada x y salida y respectivamente 
#de una funcion, representando los retardos correspondientes en el tiempo
