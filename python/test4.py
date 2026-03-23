import matplotlib
matplotlib.use("QtAgg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("dark_background")

x = np.linspace(0, 1, 50)
phi = np.linspace(0, 2*np.pi, 50)
fig, ax = plt.subplots()

markerline, stemlines, baseline = ax.stem(x, np.sin(2*np.pi*x))

ax.set_xlim(0, 1)
ax.set_ylim(-1.2, 1.2)
ax.grid(True)

# --- animation ---
def update(frame):
    y = np.sin((2*np.pi*1*x)+phi[frame])

    markerline.set_ydata(y)
    stemlines.set_segments([[[xi, 0], [xi, yi]] for xi, yi in zip(x, y)])

    return markerline, stemlines

ani = FuncAnimation(fig, update, frames=range(1, 60), interval=1450)

plt.show()
