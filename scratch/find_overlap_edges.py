import os
from PIL import Image, ImageDraw
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
arr = np.array(cards)

# In cards, Card 2 (the middle-top card) has a white border on its left side.
# Let's inspect rows y=20 to y=350 around x=200..320 to find Card 2's left white edge!
card2_left_pts = []

for y in range(20, 320):
    # Search from x=200 to x=320
    for x in range(200, 320):
        # Card 2's white border has R>200, G>200, B>200
        # and it is to the right of Card 1's photo (which has R<180 or is different)
        c = arr[y, x]
        if c[0] > 210 and c[1] > 210 and c[2] > 210:
            # Check if this is the start of Card 2's border
            card2_left_pts.append((x, y))
            break

card2_left_pts = np.array(card2_left_pts)
print(f"Card 2 left edge points found: {len(card2_left_pts)}")
if len(card2_left_pts) > 0:
    print(f"Top-most: {card2_left_pts[0]}, Bottom-most: {card2_left_pts[-1]}")
    # Fit line
    p = np.polyfit(card2_left_pts[:, 1], card2_left_pts[:, 0], 1)
    print(f"Card 2 left edge line: x = {p[0]:.4f} * y + {p[1]:.4f}")

# Also Card 3 (the bottom card):
# Card 3 is around x=250..550, y=280..480
# Let's find Card 3's top-left / left edge where it overlaps Card 1 (around y=300..450, x=150..300)
card3_pts = []
for y in range(280, 480):
    for x in range(150, 320):
        c = arr[y, x]
        if c[0] > 210 and c[1] > 210 and c[2] > 210:
            card3_pts.append((x, y))
            break

card3_pts = np.array(card3_pts)
print(f"Card 3 edge points found: {len(card3_pts)}")
if len(card3_pts) > 0:
    print(f"Card 3 edge: top-most {card3_pts[0]}, bottom-most {card3_pts[-1]}")
