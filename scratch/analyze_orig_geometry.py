import os
from PIL import Image
import numpy as np

orig = Image.open('scratch/orig_cards_binary.png').convert('RGB')
arr = np.array(orig)

# Let's inspect the left card in orig (396, 250):
# Background color: #5a000f -> [90, 0, 15]
# Let's find all non-background pixels belonging to Card 1 in orig:
bg = np.array([90, 0, 15], dtype=float)
diff = np.linalg.norm(arr.astype(float) - bg, axis=2)
is_card = diff > 25

# Card 1 is in the left region x < 150
y_idx, x_idx = np.where(is_card[:, :150])
print(f"Card 1 in orig (396x250): x in [{x_idx.min()}, {x_idx.max()}], y in [{y_idx.min()}, {y_idx.max()}]")

# Let's find the 4 corners of the left card in orig:
# Top edge, Left edge, Bottom edge, Right edge:
# Let's detect the rotation angle and corners of Card 1:
best_theta = 0
best_area = float('inf')
best_bbox = None

for theta_deg in np.linspace(-30, 30, 601):
    theta = np.radians(theta_deg)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    
    xr = x_idx * cos_t + y_idx * sin_t
    yr = -x_idx * sin_t + y_idx * cos_t
    
    w = xr.max() - xr.min()
    h = yr.max() - yr.min()
    area = w * h
    if area < best_area:
        best_area = area
        best_theta = theta_deg
        best_bbox = (xr.min(), xr.max(), yr.min(), yr.max(), w, h)

print(f"Optimal rotation angle theta: {best_theta:.2f} degrees")
print(f"Rotated bounding box: w={best_bbox[4]:.2f}, h={best_bbox[5]:.2f}")

theta = np.radians(best_theta)
cos_t, sin_t = np.cos(theta), np.sin(theta)
xmin, xmax, ymin, ymax, w, h = best_bbox

corners_rot = [
    (xmin, ymin),
    (xmax, ymin),
    (xmax, ymax),
    (xmin, ymax)
]
for xr, yr in corners_rot:
    xo = xr * cos_t - yr * sin_t
    yo = xr * sin_t + yr * cos_t
    print(f"Corner in orig: ({xo:.1f}, {yo:.1f})")
