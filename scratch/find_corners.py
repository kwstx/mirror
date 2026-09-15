import os
from PIL import Image, ImageDraw
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
arr = np.array(cards)

# Let's inspect the left card in cards
# The white border of the left card has very distinct bright pixels (>200, >200, >200)
# Let's find all pixels in x in [0, 300], y in [0, 420] that are white border
white_mask = (arr[:420, :300, 0] > 190) & (arr[:420, :300, 1] > 190) & (arr[:420, :300, 2] > 190)

# Also let's inspect the inner photo pixels
# The inner photo has background pixels that are not #5a000f and not white
bg = np.array([90, 0, 15], dtype=float)
diff = np.linalg.norm(arr[:420, :300, :3].astype(float) - bg, axis=2)
non_bg = diff > 30

# The card region is connected non_bg
from scipy.ndimage import label
lbl, num = label(non_bg)
# Find the label that contains the center of the left card (e.g. x=120, y=200)
card_lbl = lbl[200, 120]
left_card_mask = (lbl == card_lbl)

# Let's find the corners of left_card_mask
y_c, x_c = np.where(left_card_mask)
print(f"Left card bounds: x in [{x_c.min()}, {x_c.max()}], y in [{y_c.min()}, {y_c.max()}]")

# Let's find the 4 outer corners of the card quadrilateral by finding the 4 extreme lines:
# A rectangle rotated by angle theta:
# x' = x*cos(theta) + y*sin(theta)
# y' = -x*sin(theta) + y*cos(theta)
# Let's find theta that minimizes the bounding box in rotated coordinates!

best_theta = 0
best_area = float('inf')
best_bbox = None

for theta_deg in np.linspace(-30, 30, 601):
    theta = np.radians(theta_deg)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    
    xr = x_c * cos_t + y_c * sin_t
    yr = -x_c * sin_t + y_c * cos_t
    
    w = xr.max() - xr.min()
    h = yr.max() - yr.min()
    area = w * h
    if area < best_area:
        best_area = area
        best_theta = theta_deg
        best_bbox = (xr.min(), xr.max(), yr.min(), yr.max(), w, h)

print(f"Optimal rotation angle theta: {best_theta:.2f} degrees")
print(f"Rotated bounding box: w={best_bbox[4]:.2f}, h={best_bbox[5]:.2f}")
print(f"xr in [{best_bbox[0]:.2f}, {best_bbox[1]:.2f}], yr in [{best_bbox[2]:.2f}, {best_bbox[3]:.2f}]")

# Let's reconstruct the 4 unrotated corners:
theta = np.radians(best_theta)
cos_t, sin_t = np.cos(theta), np.sin(theta)
xmin, xmax, ymin, ymax, w, h = best_bbox

# Corners in rotated frame: (xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)
# Inverse rotation: x = xr*cos - yr*sin, y = xr*sin + yr*cos
corners_rot = [
    (xmin, ymin),
    (xmax, ymin),
    (xmax, ymax),
    (xmin, ymax)
]
corners_orig = []
for xr, yr in corners_rot:
    xo = xr * cos_t - yr * sin_t
    yo = xr * sin_t + yr * cos_t
    corners_orig.append((xo, yo))
    print(f"Corner: ({xo:.1f}, {yo:.1f})")

# Let's save a visualization with the rectangle drawn
vis = cards.copy()
draw = ImageDraw.Draw(vis)
draw.polygon([(round(x), round(y)) for x, y in corners_orig], outline=(255, 255, 0), width=2)
vis.save('scratch/left_card_fitted.png')
print("Saved left_card_fitted.png")
