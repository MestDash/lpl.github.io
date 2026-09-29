#!/usr/bin/env python3
"""Blur-boundary transition measurement for the frosted-glass test page.

Background: 45-degree stripes, ~28px period along any axis.
- SHARP area: local high-frequency energy spikes near every stripe boundary
  (a windowed MAX over one period is always high).
- BLURRED area: blur(12px) kills the spikes; windowed max is ~0 everywhere.

So E(x) = max of local energy over [x-14, x+14] is a clean sharp/blur probe,
and the width of the E(x) ramp at the panel's left edge = the fade width
(0 => hard edge).
"""
from PIL import Image

def load(path):
    im = Image.open(path).convert("L")
    W, H = im.size
    return im, W, H, im.load()

def energy_at(px, x, y, W):
    tot, n = 0, 0
    for k in (1, 2, 3, 4):
        for s in (-1, 1):
            xi = x + s * k
            if 0 <= xi < W:
                tot += abs(px[x, y] - px[xi, y])
                n += 1
    return tot / n

def E_profile(px, W, H, y, x0, x1, step=2):
    vals = []
    x = x0
    while x <= x1:
        m = 0.0
        for d in range(-14, 15):
            xi = x + d
            if 0 <= xi < W:
                m = max(m, energy_at(px, xi, y, W))
        vals.append((x, m))
        x += step
    return vals

def lum_window(px, W, H, x, y, r=14):
    tot, n = 0, 0
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            xi, yi = x + dx, y + dy
            if 0 <= xi < W and 0 <= yi < H:
                tot += px[xi, yi]
                n += 1
    return tot / n

GEOM = {"A": 224, "B": 208, "C": 212, "E": 232}  # box left edges

for name in ("A", "B", "C", "E"):
    im, W, H, px = load(f"frosted_{name}.png")
    y = H // 2
    vals = E_profile(px, W, H, y, 170, 430)
    e_sharp = max(e for x, e in vals if x < 205)   # outside box, left
    e_blur = max(e for x, e in E_profile(px, W, H, y, 435, 465, 2))
    gap = e_sharp - e_blur
    print(f"--- variant {name}: box left edge x={GEOM[name]}, "
          f"sharp-maxE={e_sharp:.1f}, blur-maxE={e_blur:.1f}")
    hi_t, lo_t = e_blur + 0.75 * gap, e_blur + 0.25 * gap
    edge = GEOM[name]
    cross_hi = next((x for x, e in vals if x >= edge - 2 and e < hi_t), None)
    cross_lo = next((x for x, e in vals if x >= edge - 2 and e < lo_t), None)
    if cross_hi is not None and cross_lo is not None:
        print(f"   E(x) ramp 75%->25% of gap: x={cross_hi}..{cross_lo} "
              f"=> fade width ~{cross_lo - cross_hi}px")
    else:
        print(f"   ramp not completed inside window: hi={cross_hi} lo={cross_lo}")
    # print sparse profile
    print("   " + "  ".join(f"{x}:{e:.0f}" for x, e in vals[::4]))
    print()

# D: mask-on-tint check via windowed luminance (28px period -> stable mean)
im, W, H, px = load("frosted_D.png")
y = H // 2
print("--- variant D (no blur, 60% tint, dual mask): windowed luminance ---")
for x in (190, 210, 220, 235, 250, 270, 290, 310, 330, 345, 380, 450):
    print(f"   x={x:4d}  lum={lum_window(px, W, H, x, y):6.1f}")
