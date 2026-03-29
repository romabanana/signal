import guandong as g
import matplotlib.pyplot as plt



# ti, tf, fm, fs, phi 
t, y= g.gen_sen(0, 1, 100, 1, 0)

t, w= g.gen_sinc(0, 1, 100, 1, 0)



plt.style.use("dark_background")
plt.title("Señal senoidal de 1 Hz")
plt.grid(True)
plt.stem(t, y)
plt.stem(t, w)
plt.show()
    
