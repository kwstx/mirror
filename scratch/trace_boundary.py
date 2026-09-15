import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

cards_orig = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
arr = np.array(cards_orig)

# Let's inspect where Card 2's white border and shadow are:
# For every row y from 0 to 500:
# Where does Card 2 or Card 3 start (from left to right)?
# Let's find the left boundary of Card 2 and Card 3.

card23_boundary_x = []
for y in range(500):
    # Scan from x=200 to x=320
    # Card 2 or Card 3 has its outer left edge:
    # Notice: Card 2 has a white border (R>200, G>200, B>200) or its drop shadow onto Card 1.
    # In cards_orig, let's find the exact point where Card 2/3 begins:
    # At y < 20: background
    # At y in 20..290: Card 2
    # At y in 290..480: Card 3
    found_x = None
    if y < 20:
        found_x = 248
    elif y <= 290:
        # Card 2 left edge:
        # Look for white border
        for x in range(210, 270):
            c = arr[y, x]
            if c[0] > 200 and c[1] > 200 and c[2] > 200:
                found_x = x
                break
        if found_x is None:
            found_x = int(round(0.0899 * y + 235.5))
    elif y <= 420:
        # Between y=290 and 420, Card 3 or Card 1:
        # Card 3 left edge has white border:
        for x in range(150, 320):
            c = arr[y, x]
            if c[0] > 200 and c[1] > 200 and c[2] > 200:
                # Check if it's Card 3's white border
                # Card 3 is tilted clockwise/counter-clockwise
                found_x = x
                break
        if found_x is None:
            found_x = 270
    else:
        found_x = 350
    card23_boundary_x.append(found_x)

print("Boundary samples:", [(y, card23_boundary_x[y]) for y in range(0, 500, 50)])
