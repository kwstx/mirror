import os
from PIL import Image, ImageDraw
import numpy as np

img = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
arr = np.array(img)

# Let's find the 4 corners of the card in user_orig:
# 1. Top-Left Corner (TL):
# Where the top white border meets the left white border.
# Let's find all pixels in the white border near the top-left corner:
# In img, top-left is around x: 30..50, y: 0..30
# Let's inspect rows 0..30 and cols 30..60:
for y in range(0, 30):
    for x in range(30, 60):
        c = arr[y, x]
        if c[0] > 180 and c[1] > 180 and c[2] > 180:
            print(f"TL white pixel at x={x}, y={y}: {c}")
            break
    if c[0] > 180 and c[1] > 180 and c[2] > 180:
        break

# Let's find the line of the left edge:
# For y in range(10, 260, 5): find the first white pixel or transition from red bg [81, 0, 14] to card
left_pts = []
for y in range(5, 265, 5):
    for x in range(0, 100):
        c = arr[y, x].astype(float)
        # distance from bg [81, 0, 14]
        if np.linalg.norm(c - np.array([81, 0, 14])) > 30:
            left_pts.append((x, y))
            break

left_pts = np.array(left_pts)
p_l = np.polyfit(left_pts[:, 1], left_pts[:, 0], 1)
print(f"Left edge line: x = {p_l[0]:.4f} * y + {p_l[1]:.4f}")
angle_left = np.degrees(np.arctan(p_l[0]))
print(f"Angle of left edge from vertical: {angle_left:.2f} degrees")

# Top edge line:
# For x in range(40, 250, 5): find the first non-bg pixel from y=0 downwards
top_pts = []
for x in range(40, 250, 5):
    for y in range(0, 50):
        c = arr[y, x].astype(float)
        if np.linalg.norm(c - np.array([81, 0, 14])) > 30:
            top_pts.append((x, y))
            break

top_pts = np.array(top_pts)
p_t = np.polyfit(top_pts[:, 0], top_pts[:, 1], 1)
print(f"Top edge line: y = {p_t[0]:.4f} * x + {p_t[1]:.4f}")
angle_top = np.degrees(np.arctan(p_t[0]))
print(f"Angle of top edge from horizontal: {angle_top:.2f} degrees")

# Intersection of top edge and left edge = Top-Left corner (TL)!
# x = p_l[0] * y + p_l[1]
# y = p_t[0] * x + p_t[1]
# y = p_t[0] * (p_l[0] * y + p_l[1]) + p_t[1] = p_t[0]*p_l[0]*y + p_t[0]*p_l[1] + p_t[1]
# y * (1 - p_t[0]*p_l[0]) = p_t[0]*p_l[1] + p_t[1]
tl_y = (p_t[0] * p_l[1] + p_t[1]) / (1 - p_t[0] * p_l[0])
tl_x = p_l[0] * tl_y + p_l[1]
print(f"Exact TL corner: ({tl_x:.2f}, {tl_y:.2f})")
