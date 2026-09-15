import os
from PIL import Image
import numpy as np
from scipy import ndimage

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
cards_arr = np.array(cards)

# Let's inspect the left card in detail
# What are the 4 corners of the left card?
# Let's find the outer border of the left card and the photo inner area of the left card.
# The card has a white/light frame and an inner photo.

# Let's save a zoomed-in grid or sliced image of the left card to understand its structure.
left_part = cards.crop((0, 0, 360, 420))
left_part.save('scratch/left_card_detail.png')

# Let's find the angle of the left card's edges.
# We can find edges using Sobel/gradient filter
gray = np.mean(cards_arr[:420, :360], axis=2)
sx = ndimage.sobel(gray, axis=1)
sy = ndimage.sobel(gray, axis=0)
edges = np.hypot(sx, sy)

# Threshold edges
strong_edges = edges > 50
Image.fromarray((strong_edges * 255).astype(np.uint8)).save('scratch/left_edges.png')
print("Saved left_edges.png")
