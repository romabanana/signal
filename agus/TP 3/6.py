import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fm, signal = wavfile.read('TP 3 - datasets/escala.wav')
signal = signal.astype(float)

t = np.arange(len(signal)) / fm
bloque = int(len(t) / 8)
for i in range(8):
    segmento = signal[i*bloque:(i+1)*bloque]

    sig_la = np.sin(2*np.pi * 440.00 * t[:bloque])
    parecido = np.dot(segmento, sig_la) / (np.sqrt(np.sum(segmento**2)) * np.sqrt(np.sum(sig_la**2)))
    if parecido > 0.9:
        print(f"La nota {i+1} se parece a La")