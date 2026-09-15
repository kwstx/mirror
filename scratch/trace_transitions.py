import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
arr = np.array(cards)

# Let's inspect the left card:
# The left card has:
# 1. Top edge: runs from (0, ~42) to where it goes under the center card or ends.
# 2. Left edge: runs from (0, ~42) down to (~26, ~338)? Wait, let's trace the left edge:
# At y=50, x is near 0. At y=300, x is near 25.
# Let's check slope: dx / dy = (25 - 0) / (300 - 50) = 25 / 250 = +0.10 -> angle is ~ -5.7 degrees (tilted counter-clockwise or clockwise?)
# As y increases, x increases -> tilted counter-clockwise: top is further left, bottom is further right.
# Let's find the exact angle and 4 corners of the white polaroid border and the inner photo rectangle!

# Let's write a script to sample lines across the left photo:
# Let's find the white border lines of the left photo:
# The photo itself has 4 edges:
# - Left inner edge (border between white polaroid and photo)
# - Top inner edge
# - Right inner edge
# - Bottom inner edge

# Let's scan along several horizontal lines y=100, 150, 200, 250, 300 to find:
# [bg -> outer white -> photo -> outer white -> ...]
for y in [100, 150, 200, 250, 300]:
    row = arr[y, :300]
    print(f"\n--- Y = {y} ---")
    # find transitions:
    # bg is ~[90, 0, 15]
    # white is ~[240+, 240+, 240+]
    # photo is darker
    for x in range(0, 280):
        c = row[x]
        # print if white
        if c[0] > 200 and c[1] > 200 and c[2] > 200:
            print(f"White at x={x}: {c}")
            break
    # Find transition from white to photo
    for x2 in range(x, 280):
        c = row[x2]
        if not (c[0] > 200 and c[1] > 200 and c[2] > 200):
            print(f"Photo starts at x={x2}: {c}")
            break
    # Find transition from photo to right white border
    for x3 in range(x2 + 50, 280):
        c = row[x3]
        if c[0] > 200 and c[1] > 200 and c[2] > 200:
            print(f"Right white border starts at x={x3}: {c}")
            break
