import numpy as np 

# gen_sen: genera senoidal. 

def gen_sen(ti, tf, fm, fs, phi):
    if tf <= ti:
       raise ValueError("tf < ti!!")

    delta_t = tf-ti # muestras por segundo
    t = np.linspace(ti, tf, delta_t*fm)
    x = (2*np.pi*fs*t) + phi #2*pi*fs*t + phi
    y = np.sin(x)
    return t, y

def gen_sinc(ti, tf, fm, fs, phi):
    if tf <= ti:
       raise ValueError("tf < ti!!")

    delta_t = tf-ti # muestras por segundo
    t = np.linspace(ti, tf, delta_t*fm)
    x = (2*np.pi*fs*t) + phi #2*pi*fs*t + phi
    y = np.where(x == 0, 1, np.sin(x)/x)
    return t, y

def gen_cuad(ti, tf, fm, fs, phi):
    if tf <= ti:
        raise ValueError("tf < ti!!")

    delta_t = tf-ti # muestras por segundo
    t = np.linspace(ti, tf, delta_t*fm)
    x = (2*np.pi*fs*t) + phi #2*pi*fs*t + phi
    mod = np.mod(x, 2*np.pi)
    y = np.where(mod >= np.pi, 1, -1)
    return t, y
