import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Load the original high-res cards image from the reference
orig_1x = Image.open('scratch/true_orig_cards.png').convert('RGBA') # (395, 250)
orig_2x = orig_1x.resize((792, 500), Image.Resampling.LANCZOS) # (792, 500)
arr_orig = np.array(orig_2x)

# Let's inspect the 4 cards in orig_2x (792 x 500):
# We will create clean polygonal masks for each of the 4 cards.
# Card 1 (Left):
# TL: (14, 23), TR: (252, 10), BR: (268, 324), BL: (30, 337)
# Card 2 (Top-Center):
# TL: (244, 28), TR: (508, 6), BR: (526, 316), BL: (262, 338)
# Card 3 (Bottom-Center):
# TL: (152, 316), TR: (416, 294), BR: (432, 494), BL: (168, 500)
# Card 4 (Right):
# TL: (456, 178), TR: (648, 192), BR: (628, 488), BL: (436, 474)

# Let's verify the exact corners of all 4 cards in orig_2x:
# Let's write a script that extracts each card cleanly with its exact quad,
# applies a clean thin white border, and composites them on pure white with soft shadows!
