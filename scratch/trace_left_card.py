import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
arr = np.array(cards)
bg = np.array([90, 0, 15], dtype=float)

# Let's find all boundary points between the left card and the background
# Left card is on the left side (x < 350)
left_mask = np.zeros((500, 350), dtype=bool)
for y in range(500):
    for x in range(350):
        c = arr[y, x].astype(float)
        # Check if significantly different from background [90, 0, 15]
        # In shadow or border
        if np.linalg.norm(c - bg) > 25:
            left_mask[y, x] = True

# Let's inspect where the left card is
y_pts, x_pts = np.where(left_mask)
print(f"Mask bounds: y=[{y_pts.min()}, {y_pts.max()}], x=[{x_pts.min()}, {x_pts.max()}]")

# Let's find the 4 corners of the outer card:
# Top-most point, Left-most point, Bottom-most point, Right-most point (or corners)
# We can find the convex hull or fit lines to the 4 edges!
from scipy.spatial import ConvexHull
pts = np.column_stack((x_pts, y_pts))
hull = ConvexHull(pts)
hull_pts = pts[hull.vertices]

print("Convex hull vertices:")
for p in hull_pts:
    print(p)

# Save mask image
Image.fromarray((left_mask * 255).astype(np.uint8)).save('scratch/left_mask.png')
print("Saved left_mask.png")
