import numpy as np
import time
from numpy._core.function_base import linspace
from rich.console import Console

console = Console()

WIDTH = console.size.width 
HEIGHT = console.size.height - 2

def render_wave(y):
    canvas = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for i, val in enumerate(y):
        row = int((1 - val) * (HEIGHT // 2))
        row = max(0, min(HEIGHT-1, row))
        canvas[row][i] = "█"

    return "\n".join("".join(row) for row in canvas)

x = np.linspace(0, 1, WIDTH)
phis = linspace(0,12*np.pi,100)
for phi in phis:
    y = np.random.uniform(0.25, 0.6) * np.sin((np.random.uniform(1, 4) *  2 * np.pi * x) + phi)

    #y = np.sin(( 2 * np.pi * x) + phi)
    #console.clear()
    console.print(render_wave(y))
    #console.print(f"Frequency: {1} Hz")

    time.sleep(0.1)
