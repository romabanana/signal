import numpy as np
import time
from rich.console import Console

console = Console()

WIDTH = 80
HEIGHT = 24

def render_wave(y):
    canvas = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for i, val in enumerate(y):
        row = int((1 - val) * (HEIGHT // 2))
        row = max(0, min(HEIGHT-1, row))
        canvas[row][i] = "█"

    return "\n".join("".join(row) for row in canvas)

x = np.linspace(0, 1, WIDTH)

for fs in range(1, 40):
    y = np.sin(2 * np.pi * fs * x)

    console.clear()
    console.print(render_wave(y))
    console.print(f"Frequency: {fs} Hz")

    time.sleep(0.5)
