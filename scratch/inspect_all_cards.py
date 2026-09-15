import os
from PIL import Image, ImageDraw
import numpy as np

cards_orig = Image.open('public/images/party_of_four_cards.png').convert('RGB')
arr = np.array(cards_orig)

# Let's find all white borders in cards_orig:
r = arr[:, :, 0].astype(float)
g = arr[:, :, 1].astype(float)
b = arr[:, :, 2].astype(float)
is_white = (r > 190) & (g > 190) & (b > 190) & (np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b) < 40)

# Save white map
Image.fromarray((is_white * 255).astype(np.uint8)).save('scratch/all_white_borders.png')

# Let's inspect the cards:
# Let's find out how many cards and where they are:
# Card 1: left card (blond guy)
# Card 2: center top card
# Card 3: center bottom card
# Card 4: right card

print("Saved all_white_borders.png")
