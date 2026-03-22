import matplotlib
matplotlib.use("QtAgg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Style ---
plt.style.use("dark_background")

plt.rcParams.update({
    "axes.facecolor": "#0a0a0a",
    "figure.facecolor": "#0a0a0a",
    "axes.edgecolor": "#444",
    "axes.labelcolor": "#ddd",
    "xtick.color": "#888",
    "ytick.color": "#888",
    "grid.color": "#222",
    "lines.linewidth": 2,
})

# --- Data ---
x = np.linspace(0, 1, 1000)

# --- Figure ---
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(2*np.pi*x), color="#00ff9f")

ax.set_xlim(0, 1)
ax.set_ylim(-1.2, 1.2)
ax.grid(True, linestyle="--", linewidth=0.5)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

title = ax.set_title("Frequency: 1 Hz", color="#00ff9f")

# --- Animation function ---
def update(frame):
    fs = frame
    y = np.sin(2*np.pi*fs*x)

    line.set_ydata(y)
    title.set_text(f"Frequency: {fs} Hz")

    return line, title

# --- Animate ---
ani = FuncAnimation(
    fig,
    update,
    frames=range(1, 60),
    interval=50,   # ms between frames
    blit=True
)

plt.show()
