import os
from PIL import Image
import numpy as np

cards = Image.open('scratch/true_orig_cards.png').convert('RGB')
arr = np.array(cards)
bg = np.array([90, 0, 15], dtype=float)

# Find all pixels of Card 1 (only Card 1):
# In true_orig_cards (395, 250):
# Card 1 is in x in [0, 130], y in [0, 180]
# Card 2 is on the right: Card 2 has a white border starting at (118, 0) down to (128, 140)
# Card 3 is at the bottom: Card 3 starts around y=140, x=70

card1_mask = np.zeros((250, 395), dtype=bool)
for y in range(0, 180):
    for x in range(0, 140):
        c = arr[y, x].astype(float)
        if np.linalg.norm(c - bg) > 25:
            # Check if left of Card 2's white border
            card2_edge_x = int(0.09 * y + 118)
            card3_edge_x = int(0.4 * (y - 140) + 75) if y >= 140 else 999
            if x < card2_edge_x and x < card3_edge_x:
                card1_mask[y, x] = True

y_pts, x_pts = np.where(card1_mask)
print(f"Card 1 mask points: count={len(x_pts)}, x in [{x_pts.min()}, {x_pts.max()}], y in [{y_pts.min()}, {y_pts.max()}]")

# Let's find the 4 edges of Card 1:
# Top edge:
top_edge = []
for x in range(x_pts.min(), x_pts.max() + 1):
    ys = np.where(card1_mask[:, x])[0]
    if len(ys) > 0:
        top_edge.append((x, ys.min()))
top_edge = np.array(top_edge)
p_top = np.polyfit(top_edge[:, 0], top_edge[:, 1], 1)
print(f"Top edge: y = {p_top[0]:.4f} * x + {p_top[1]:.4f}")

# Left edge:
left_edge = []
for y in range(y_pts.min(), y_pts.max() + 1):
    xs = np.where(card1_mask[y, :])[0]
    if len(xs) > 0:
        left_edge.append((xs.min(), y))
left_edge = np.array(left_edge)
p_left = np.polyfit(left_edge[:, 1], left_edge[:, 0], 1)
print(f"Left edge: x = {p_left[0]:.4f} * y + {p_left[1]:.4f}")

# TL corner:
tl_y = (p_top[0] * p_left[1] + p_top[1]) / (1 - p_top[0] * p_left[0])
tl_x = p_left[0] * tl_y + p_left[1]
print(f"TL corner: ({tl_x:.2f}, {tl_y:.2f})")

# Tilt angle from vertical:
angle_deg = np.degrees(np.arctan(p_left[0]))
print(f"Card tilt angle: {angle_deg:.2f} degrees")
