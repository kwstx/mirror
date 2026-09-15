import os
from PIL import Image
import numpy as np

crop = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
arr = np.array(crop)

# Let's inspect the borders of the photo card in media_1789473470465.png
# Background color is dark red #5a000f or similar:
bg = np.array([81, 0, 14], dtype=float)

# Let's find the white border of the photo card in crop:
# In crop, there is a thin white line on the top, left, etc.
# Let's print out the coordinates of the white border pixels in crop!
r = arr[:, :, 0].astype(float)
g = arr[:, :, 1].astype(float)
b = arr[:, :, 2].astype(float)
is_white = (r > 160) & (g > 160) & (b > 160)

y_w, x_w = np.where(is_white)
print(f"White pixels in crop: count={len(x_w)}, x in [{x_w.min()}, {x_w.max()}], y in [{y_w.min()}, {y_w.max()}]")

# Let's find the lines of the photo frame:
# Left edge line in crop:
# Top edge line in crop:
# Bottom edge line in crop:
# Right edge line in crop:

# Save a map of the white border
Image.fromarray((is_white * 255).astype(np.uint8)).save('scratch/crop_white_map.png')
print("Saved scratch/crop_white_map.png")
