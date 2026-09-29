#!/usr/bin/env python3
"""ASCII-render a crop of a screenshot so we can 'see' the pattern."""
from PIL import Image
import sys

RAMP = " .:-=+*#%@"

def render(path, x0, x1, y0, y1, step=2):
    im = Image.open(path).convert("L")
    px = im.load()
    print(f"### {path}  x {x0}..{x1}  y {y0}..{y1} (step {step})")
    for y in range(y0, y1, step):
        row = ""
        for x in range(x0, x1, step):
            v = px[x, y]
            row += RAMP[min(len(RAMP) - 1, v * len(RAMP) // 256)]
        print(f"{y:4d} {row}")

if __name__ == "__main__":
    p = sys.argv[1]
    render(p, 180, 340, 230, 270)
