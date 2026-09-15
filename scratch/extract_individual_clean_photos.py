import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Load the original uncropped reference
orig_2x = Image.open('scratch/true_orig_cards.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)

# Let's inspect each card's center and rotation angle:
# 1. Card 1 (Left):
# Center: cx1 = 131, cy1 = 180, angle = 5.02 deg
# 2. Card 2 (Top-Center):
# Center: cx2 = 380, cy2 = 168, angle = -4.8 deg
# 3. Card 3 (Bottom-Center):
# Center: cx3 = 286, cy3 = 398, angle = 3.5 deg
# 4. Card 4 (Right):
# Center: cx4 = 605, cy4 = 338, angle = -6.2 deg

# Let's write a script to unrotate and crop each photo cleanly from orig_2x!
