import os
from PIL import Image
import numpy as np

crop = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
arr = np.array(crop)

# Let's inspect where the card boundary is:
# On the left: at each y, where does the dark red background [81, 0, 14] end and the card begin?
bg = np.array([81, 0, 14], dtype=float)

left_boundary = []
for y in range(0, arr.shape[0], 5):
    for x in range(0, arr.shape[1]):
        c = arr[y, x].astype(float)
        # Check distance from bg
        if np.linalg.norm(c - bg) > 25:
            left_boundary.append((x, y))
            break

left_boundary = np.array(left_boundary)
p_left = np.polyfit(left_boundary[:, 1], left_boundary[:, 0], 1)
print(f"Left edge in crop: x = {p_left[0]:.4f} * y + {p_left[1]:.4f}")
angle_deg = np.degrees(np.arctan(p_left[0]))
print(f"Card tilt angle in user's crop: {angle_deg:.2f} degrees")

# Top boundary:
top_boundary = []
for x in range(int(p_left[1]), arr.shape[1], 5):
    for y in range(0, arr.shape[0]):
        c = arr[y, x].astype(float)
        if np.linalg.norm(c - bg) > 25:
            top_boundary.append((x, y))
            break

top_boundary = np.array(top_boundary)
if len(top_boundary) > 0:
    p_top = np.polyfit(top_boundary[:, 0], top_boundary[:, 1], 1)
    print(f"Top edge in crop: y = {p_top[0]:.4f} * x + {p_top[1]:.4f}")
    angle_top_deg = np.degrees(np.arctan(p_top[0]))
    print(f"Top edge tilt angle: {angle_top_deg:.2f} degrees")
