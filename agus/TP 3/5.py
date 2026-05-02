import numpy as np
import matplotlib.pyplot as plt

signal = np.loadtxt('TP 3 - datasets/te.txt')
fm = 11025

filas = [697,770,852,941]
columnas = [1209,1336,1477]

teclado = {
    (697,1209): '1',
    (697,1336): '2',
    (697,1477): '3',

    (770,1209): '4',
    (770,1336): '5',
    (770,1477): '6',

    (852,1209): '7',
    (852,1336): '8',
    (852,1477): '9',

    (941,1209): '*',
    (941,1336): '0',
    (941,1477): '#'
}

amplitud = np.abs(signal)
umbral = 0.4 * np.max(amplitud)
signal_filtered = np.where(amplitud > umbral, signal, 0)

divisiones = 11
bloque = int((len(signal) / divisiones))
teclas = ['?']*divisiones
t = np.arange(bloque) / fm
for i in range(divisiones):
    #segmento = signal[i*bloque:(i+1)*bloque]
    segmento = signal_filtered[i*bloque:(i+1)*bloque]
    plt.plot(t, segmento)
    #plt.show()

    mejor_parecido = -1
    mejor_tecla = '?'

    for f in filas:
        for c in columnas:

            plantilla = (np.sin(2 * np.pi * f * t) + np.sin(2 * np.pi * c * t))
            parecido = np.dot(segmento, plantilla) / (np.sqrt(np.sum(segmento**2)) * np.sqrt(np.sum(plantilla**2)))

            if parecido > mejor_parecido and parecido > 0.014:
                mejor_parecido = parecido
                mejor_tecla = teclado.get((f,c), '?')
    teclas[i] = mejor_tecla
print(teclas)