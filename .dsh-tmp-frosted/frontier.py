#!/usr/bin/env python3
"""Row-by-row 'sharpness frontier': rightmost x where sharp stripes remain.
A mask that fades the backdrop blur -> frontier traces the mask curve.
A mask ignored by backdrop-filter -> hard vertical frontier at the box edge.
"""
from PIL import Image
import sys

def frontier(path, x0, x1, y0, y1, step=2, thresh=6):
    im = Image.open(path).convert("L")
    W, H = im.size
    px = im.load()
    print(f"### {path}")
    print("    y   frontier-x")
    for y in range(y0, y1, step):
        fx = None
        for x in range(x1, x0, -1):
            m = 0.0
            for dy in (-3, 0, 3):
                yi = y + dy
                if not (0 <= yi < H):
                    continue
                for dx in (-3, 0, 3):
                    xi = x + dx
                    if not (0 <= xi < W):
                        continue
                    m = max(m,
                            abs(px[xi, yi] - px[min(xi + 3, W - 1), yi]),
                            abs(px[xi, yi] - px[xi, min(yi + 3, H - 1)]))
            if m > thresh:
                fx = x
                break
        print(f"  {y:3d}   {fx}")

if __name__ == "__main__":
    for p in sys.argv[1:]:
        frontier(p, 180, 470, 210, 292)
        print()
