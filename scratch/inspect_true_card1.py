import os
from PIL import Image
import numpy as np

cards = Image.open('scratch/true_orig_cards.png').convert('RGB')
arr = np.array(cards)

# Let's save a crop of Card 1 from true_orig_cards
card1_crop = cards.crop((0, 0, 160, 200))
card1_crop.save('scratch/true_card1_crop.png')

# In true_orig_cards (395, 250):
# Let's find the 4 corners of Card 1:
# Card 1 has:
# - Top edge: slopes slightly from top-left (around (0, 22) or (8, 7)) to top-right
# - Left edge: slopes from top-left down-right to bottom-left (around (20, 160))
# - Bottom edge: goes from bottom-left to where it goes under Card 3
# - Right edge: goes under Card 2 (around x=118)

# Let's inspect the white border of Card 1 in true_card1_crop:
# Card 1 has a white outline/border around the photo!
# Let's find all pixels with high brightness (R,G,B > 180) in Card 1:
r, g, b = arr[:180, :150, 0], arr[:180, :150, 1], arr[:180, :150, 2]
is_white = (r > 160) & (g > 160) & (b > 160)

Image.fromarray((is_white * 255).astype(np.uint8)).save('scratch/true_card1_white.png')
print("Saved true_card1_crop.png and true_card1_white.png")
