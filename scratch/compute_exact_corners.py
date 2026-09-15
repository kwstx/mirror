import os
from PIL import Image
import numpy as np

orig_2x = Image.open('scratch/orig_cards_binary.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)
mask = Image.open('scratch/exact_orig_card1_mask.png').convert('L')
mask_arr = np.array(mask) > 128

# Let's inspect the 4 outer corners of Card 1:
# We can find the 4 corners of the polygon:
# Let's fit 4 lines to the boundary:
# Line 1 (Left edge): points on the left boundary
# Line 2 (Top edge): points on the top boundary
# Line 3 (Bottom edge): points on the bottom boundary
# Line 4 (Right edge): points on the right boundary

y_idx, x_idx = np.where(mask_arr)

# Top edge: for each x in [10, 200], min y
top_pts = []
for x in range(10, 220):
    ys = np.where(mask_arr[:, x])[0]
    if len(ys) > 0:
        top_pts.append((x, ys.min()))
top_pts = np.array(top_pts)
p_top = np.polyfit(top_pts[:, 0], top_pts[:, 1], 1)
print(f"Top line: y = {p_top[0]:.4f} * x + {p_top[1]:.4f}")

# Left edge: for each y in [30, 470], min x
left_pts = []
for y in range(30, 470):
    xs = np.where(mask_arr[y, :])[0]
    if len(xs) > 0:
        left_pts.append((xs.min(), y))
left_pts = np.array(left_pts)
p_left = np.polyfit(left_pts[:, 1], left_pts[:, 0], 1)
print(f"Left line: x = {p_left[0]:.4f} * y + {p_left[1]:.4f}")

# Bottom edge: for each x in [40, 250], max y
bottom_pts = []
for x in range(40, 260):
    ys = np.where(mask_arr[:, x])[0]
    if len(ys) > 0:
        bottom_pts.append((x, ys.max()))
bottom_pts = np.array(bottom_pts)
p_bottom = np.polyfit(bottom_pts[:, 0], bottom_pts[:, 1], 1)
print(f"Bottom line: y = {p_bottom[0]:.4f} * x + {p_bottom[1]:.4f}")

# TL corner: intersection of top line and left line
# y = p_top[0]*x + p_top[1]
# x = p_left[0]*y + p_left[1]
tl_y = (p_top[0] * p_left[1] + p_top[1]) / (1 - p_top[0] * p_left[0])
tl_x = p_left[0] * tl_y + p_left[1]

# BL corner: intersection of bottom line and left line
bl_y = (p_bottom[0] * p_left[1] + p_bottom[1]) / (1 - p_bottom[0] * p_left[0])
bl_x = p_left[0] * bl_y + p_left[1]

print(f"TL corner: ({tl_x:.2f}, {tl_y:.2f})")
print(f"BL corner: ({bl_x:.2f}, {bl_y:.2f})")

# Since the card is a rectangle:
# Vector Left = BL - TL:
v_left = np.array([bl_x - tl_x, bl_y - tl_y])
card_height = np.linalg.norm(v_left)
print(f"Card height along left edge: {card_height:.2f}")

# Vector Top is perpendicular to Vector Left:
# Normal to (vx, vy) is (-vy, vx) or (vy, -vx)
# Top edge goes rightwards: so (vy, -vx)
u_top = np.array([v_left[1], -v_left[0]]) / card_height

# Let's find card width from top edge:
# The top edge goes until around x=280..
card_width = 285.0 # standard width

# TR = TL + card_width * u_top
tr = np.array([tl_x, tl_y]) + card_width * u_top
# BR = BL + card_width * u_top
br = np.array([bl_x, bl_y]) + card_width * u_top

print(f"TR corner: ({tr[0]:.2f}, {tr[1]:.2f})")
print(f"BR corner: ({br[0]:.2f}, {br[1]:.2f})")
