import os
from PIL import Image
import numpy as np

orig_2x = Image.open('scratch/orig_cards_binary.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
arr_orig = np.array(orig_2x)
bg = np.array([90, 0, 15], dtype=float)

# In orig_2x, let's find the exact pixel mask of Card 1 (only Card 1, excluding Cards 2, 3, 4):
# Cards 2, 3, 4 are to the right.
# Let's inspect the mask of Card 1 in orig_2x:
mask_card1 = np.zeros((500, 792), dtype=bool)

# Card 2 left edge: x = 0.0899 * y + 235.5 (in 2x: x = 0.0899 * y + 246)
for y in range(500):
    for x in range(300):
        # If not background
        if np.linalg.norm(arr_orig[y, x].astype(float) - bg) > 25:
            # Check if left of Card 2 & 3 boundary
            if y < 290 and x < int(0.0899 * y + 248):
                mask_card1[y, x] = True
            elif y >= 290 and x < int(0.3 * (y - 290) + 270):
                mask_card1[y, x] = True

# Let's save the exact mask of Card 1 from orig_2x
Image.fromarray((mask_card1 * 255).astype(np.uint8)).save('scratch/exact_orig_card1_mask.png')
print("Saved exact_orig_card1_mask.png")

# Let's find the exact 4 corners of Card 1 from mask_card1:
y_pts, x_pts = np.where(mask_card1)
print(f"Exact Card 1 bounds: x in [{x_pts.min()}, {x_pts.max()}], y in [{y_pts.min()}, {y_pts.max()}]")
