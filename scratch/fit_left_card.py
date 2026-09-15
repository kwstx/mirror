import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')

cards_arr = np.array(cards)
ref_arr = np.array(ref)

print("cards shape:", cards_arr.shape)
print("ref shape:", ref_arr.shape)

# Let's inspect the left card in cards_arr
# In party_of_four_cards:
# The image is 792 wide x 500 high.
# Let's find the card's 4 outer corners and 4 inner photo corners.
# The card has a white border. Let's find the inner photo edges.
# Let's sample along horizontal and vertical lines in the left region x in [0, 350], y in [0, 450].

# Let's save a visual inspection of slices or crops
left_crop = cards.crop((0, 0, 350, 480))
left_crop.save('scratch/left_inspect.png')

# Let's detect the line segments of the photo border:
# A photo card is a rectangle rotated by angle theta:
# Top edge line: y = m*x + c1
# Bottom edge line: y = m*x + c2
# Left edge line: x = -m*y + c3
# Right edge line: x = -m*y + c4

# Let's find the slope m by checking the angle of the left edge and top edge:
# Let's inspect the white border pixels
white_mask = (cards_arr[:480, :350, 0] > 200) & (cards_arr[:480, :350, 1] > 200) & (cards_arr[:480, :350, 2] > 200)

# Let's find the outer border lines from the white mask
y_w, x_w = np.where(white_mask)
print(f"White mask point count: {len(x_w)}")

# Outer left edge: min x for each y
left_edge_pts = []
for y in range(y_w.min(), y_w.max() + 1):
    xs = np.where(white_mask[y, :])[0]
    if len(xs) > 0:
        left_edge_pts.append((xs.min(), y))

left_edge_pts = np.array(left_edge_pts)
# Fit line to left edge points
# x = slope * y + intercept
p_left = np.polyfit(left_edge_pts[:, 1], left_edge_pts[:, 0], 1)
print(f"Outer left edge: x = {p_left[0]:.4f} * y + {p_left[1]:.4f}")
angle_deg = np.degrees(np.arctan(p_left[0]))
print(f"Rotation angle from vertical: {angle_deg:.2f} degrees")

# Top edge points: min y for each x
top_edge_pts = []
for x in range(x_w.min(), x_w.max() + 1):
    ys = np.where(white_mask[:, x])[0]
    if len(ys) > 0:
        top_edge_pts.append((x, ys.min()))

top_edge_pts = np.array(top_edge_pts)
p_top = np.polyfit(top_edge_pts[:, 0], top_edge_pts[:, 1], 1)
print(f"Outer top edge: y = {p_top[0]:.4f} * x + {p_top[1]:.4f}")
angle_top_deg = np.degrees(np.arctan(p_top[0]))
print(f"Top edge angle from horizontal: {angle_top_deg:.2f} degrees")
