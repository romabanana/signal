import numpy as np
import time
import sys

WIDTH = 120
HEIGHT = 40

def braille_plot(y):
    canvas = {}

    for i, val in enumerate(y):
        # map to higher resolution grid
        x = i
        y_pos = int((1 - val) * (HEIGHT * 4 // 2))

        cx = x // 2
        cy = y_pos // 4

        dot_x = x % 2
        dot_y = y_pos % 4

        # braille dot mapping
        dots = [
            [0x1, 0x8],
            [0x2, 0x10],
            [0x4, 0x20],
            [0x40, 0x80]
        ]

        if (cx, cy) not in canvas:
            canvas[(cx, cy)] = 0

        canvas[(cx, cy)] |= dots[dot_y][dot_x]

    # render
    output = []
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH // 2):
            val = canvas.get((x, y), 0)
            row += chr(0x2800 + val)
        output.append(row)

    return "\n".join(output)


x = np.linspace(0, 1, WIDTH)

for fs in range(1, 50):
    y = np.sin(2 * np.pi * fs * x)

    print("\033[H", end="")  # move cursor to top
    print(braille_plot(y))
    print(f"Frequency: {fs} Hz")

    time.sleep(0.5)
