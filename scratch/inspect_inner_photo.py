import os
from PIL import Image, ImageDraw
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
arr = np.array(cards)

# Let's inspect the left card:
# Let's find the 4 edges of the inner photo:
# In the left card, the inner photo has a dark border / margin inside the white card.
# Let's check:
# Top edge of inner photo:
# Let's inspect column by column (x = 30 to 240) where the top white border ends and inner photo begins.
top_inner_pts = []
bottom_inner_pts = []
left_inner_pts = []
right_inner_pts = []

# Let's find the white border mask:
# The white border pixels have R, G, B > 180 and low saturation (difference between max and min channel < 30)
r = arr[:450, :350, 0].astype(float)
g = arr[:450, :350, 1].astype(float)
b = arr[:450, :350, 2].astype(float)
is_white = (r > 170) & (g > 170) & (b > 170) & (np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b) < 40)

# Save white border visualization
Image.fromarray((is_white * 255).astype(np.uint8)).save('scratch/white_border_detected.png')
print("Saved scratch/white_border_detected.png")

# Now let's trace:
# For x from 40 to 220:
# Looking down from y=20: first white border (outer edge), then end of white border (top inner edge of photo), then start of bottom white border (bottom inner edge of photo), then end of bottom white border (outer bottom edge)
for x in range(40, 220, 20):
    col = is_white[:, x]
    white_indices = np.where(col)[0]
    if len(white_indices) > 0:
        print(f"Col x={x}: white runs at y in {white_indices}")
