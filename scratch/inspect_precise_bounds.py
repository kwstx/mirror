import os
from PIL import Image
import numpy as np

orig_2x = Image.open('scratch/true_orig_cards.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)
bg = np.array([90, 0, 15], dtype=float)

# Let's inspect Card 4 (Right side):
# Where is Card 4 in orig_2x?
# Let's find all non-background pixels in x > 440, y > 150:
diff = np.linalg.norm(arr.astype(float) - bg, axis=2)
is_c4 = (diff > 25) & (np.arange(500)[:, None] > 160) & (np.arange(792)[None, :] > 440)

y_c4, x_c4 = np.where(is_c4)
print(f"Card 4 bounds: x in [{x_c4.min()}, {x_c4.max()}], y in [{y_c4.min()}, {y_c4.max()}]")

# Let's inspect the corners of Card 4:
# TL (min y or min x):
# TR (max x):
# BR (max y):
# BL (min x at bottom):
tl_4 = (x_c4[np.argmin(y_c4)], y_c4.min())
tr_4 = (x_c4.max(), y_c4[np.argmax(x_c4)])
br_4 = (x_c4[np.argmax(y_c4)], y_c4.max())
bl_4 = (x_c4.min(), y_c4[np.argmin(x_c4)])

print(f"Card 4 TL: {tl_4}, TR: {tr_4}, BR: {br_4}, BL: {bl_4}")

# Card 2 (Top-Center):
is_c2 = (diff > 25) & (np.arange(500)[:, None] < 340) & (np.arange(792)[None, :] > 240) & (np.arange(792)[None, :] < 530)
y_c2, x_c2 = np.where(is_c2)
print(f"Card 2 bounds: x in [{x_c2.min()}, {x_c2.max()}], y in [{y_c2.min()}, {y_c2.max()}]")
print(f"Card 2 TL: ({x_c2[np.argmin(y_c2)]}, {y_c2.min()}), TR: ({x_c2.max()}, {y_c2[np.argmax(x_c2)]}), BR: ({x_c2[np.argmax(y_c2)]}, {y_c2.max()}), BL: ({x_c2.min()}, {y_c2[np.argmin(x_c2)]})")

# Card 3 (Bottom-Center):
is_c3 = (diff > 25) & (np.arange(500)[:, None] > 280) & (np.arange(792)[None, :] > 140) & (np.arange(792)[None, :] < 430)
y_c3, x_c3 = np.where(is_c3)
print(f"Card 3 bounds: x in [{x_c3.min()}, {x_c3.max()}], y in [{y_c3.min()}, {y_c3.max()}]")
print(f"Card 3 TL: ({x_c3[np.argmin(y_c3)]}, {y_c3.min()}), TR: ({x_c3.max()}, {y_c3[np.argmax(x_c3)]}), BR: ({x_c3[np.argmax(y_c3)]}, {y_c3.max()}), BL: ({x_c3.min()}, {y_c3[np.argmin(x_c3)]})")
