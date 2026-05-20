import numpy as np
import matplotlib.pyplot as plt

def fourier(s):
    S = np.zeros(len(s), dtype=complex)
    for k in range(len(s)):
        for n in range(len(s)):
            S[k] += s[n] * np.exp(-2j * np.pi * k * n / len(s))
    return S

t = np.arange(0, 1, 1/100)
a = np.sin(2*np.pi * 2 * t)
b = np.where(a > 0, 1, -1)
c = np.sin(2*np.pi * 4 * t)

#1
ab = np.dot(a, b) #no ortogonales
ac = np.dot(a, c) #ortogonales
cb = np.dot(c, b) #ortogonales
print("Relación (ab/ac/cb):")
print(ab, ac, cb)

#2
A = fourier(a)
B = fourier(b)
C = fourier(c)

AB = np.vdot(A, B) #no orgononales
AC = np.vdot(A, C) #ortogonales
CB = np.vdot(C, B) #ortogonales
print("Relación (AB/AC/CB):")
print(AB, AC, CB)

#3
c3 = np.sin(2*np.pi * 3.5 * t)
C3 = fourier(c3)
ac3 = np.dot(a, c3)
print("Relación (ac3):")
print(ac3) #ortogonales, pero solo con la configuracion temporal actual permite una cancelacion ideal entre ambas frecuencias
AC3 = np.vdot(A, C3)
print("Relación (AC3):")
print(AC3) #ortogonales, un ligero cambio en t las conviernte en no ortogonales