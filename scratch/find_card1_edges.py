import os
from PIL import Image
import numpy as np

orig = Image.open('scratch/orig_cards_binary.png').convert('RGB')
arr = np.array(orig)
bg = np.array([90, 0, 15], dtype=float)

# In orig (396, 250):
# For each column x from 0 to 150: find min y and max y where pixel is not background
col_bounds = []
for x in range(0, 160):
    ys = []
    for y in range(0, 250):
        # Card 1 is only on the left (not Card 2)
        if y < 145 or (y >= 145 and x < 100):
            if np.linalg.norm(arr[y, x].astype(float) - bg) > 25:
                ys.append(y)
    if len(ys) > 0:
        col_bounds.append((x, min(ys), max(ys)))

col_bounds = np.array(col_bounds)
print(f"Card 1 x spans: [{col_bounds[:, 0].min()}, {col_bounds[:, 0].max()}]")

# Top edge points:
p_top = np.polyfit(col_bounds[:, 0], col_bounds[:, 1], 1)
print(f"Top edge: y = {p_top[0]:.4f} * x + {p_top[1]:.4f} (angle = {np.degrees(np.arctan(p_top[0])):.2f} deg)")

# Bottom edge points:
p_bot = np.polyfit(col_bounds[:, 0], col_bounds[:, 2], 1)
print(f"Bottom edge: y = {p_bot[0]:.4f} * x + {p_bot[1]:.4f} (angle = {np.degrees(np.arctan(p_bot[0])):.2f} deg)")
