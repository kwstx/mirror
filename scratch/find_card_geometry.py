import os
from PIL import Image, ImageDraw
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
arr = np.array(cards)

# Let's find the white border corners of the left card
# In cards, the left card has a white border.
# Let's find pixels where R>220, G>220, B>220 in the left 350 pixels
white_mask = (arr[:450, :350, 0] > 220) & (arr[:450, :350, 1] > 220) & (arr[:450, :350, 2] > 220)

# Let's find the 4 corners of this white quadrilateral:
# Let's find the boundary points of white_mask and photo inside
# Inside the white frame, there is a photo.
# The photo has dark background (blue couch/sofa, dark hair, beige shirt).
# Around the photo is a white polaroid border.
# Outside the white polaroid border is the dark red background #5a000f (90, 0, 15).

# Let's find the outer border lines of the left card:
# Top edge, Left edge, Bottom edge, Right edge:
# Let's inspect the mask of the card (everything inside the card, including white border and inner photo)
bg = np.array([90, 0, 15], dtype=float)
diff = np.linalg.norm(arr[:480, :350, :3].astype(float) - bg, axis=2)
card_mask = diff > 30

# Let's find the convex hull or contour of card_mask
y_idx, x_idx = np.where(card_mask)
print(f"Card bounds: x in [{x_idx.min()}, {x_idx.max()}], y in [{y_idx.min()}, {y_idx.max()}]")

# Let's find the 4 corners of the outer card:
# Top-Left corner (minimizes x + y)
# Top-Right corner (maximizes x - y or minimizes -x + y)
# Bottom-Left corner (minimizes x - y or maximizes -x + y)
# Bottom-Right corner (maximizes x + y)

# Let's evaluate extreme points:
tl_idx = np.argmin(x_idx * 1.0 + y_idx * 1.0)
tr_idx = np.argmax(x_idx * 1.0 - y_idx * 1.0)
bl_idx = np.argmin(x_idx * 1.0 - y_idx * 1.0)
br_idx = np.argmax(x_idx * 1.0 + y_idx * 1.0)

print(f"Outer TL: ({x_idx[tl_idx]}, {y_idx[tl_idx]})")
print(f"Outer TR: ({x_idx[tr_idx]}, {y_idx[tr_idx]})")
print(f"Outer BL: ({x_idx[bl_idx]}, {y_idx[bl_idx]})")
print(f"Outer BR: ({x_idx[br_idx]}, {y_idx[br_idx]})")

# Let's also inspect the inner photo area:
# The inner photo is surrounded by the white border.
# Let's find where the white border ends and the inner photo starts.
