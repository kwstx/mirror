import os
from PIL import Image, ImageDraw
import numpy as np

orig_2x = Image.open('scratch/true_orig_cards.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)
bg = np.array([90, 0, 15], dtype=float)

# Let's inspect the cards:
# Card 1 (Left guy):
# Unrotate by -5.02 deg around (131, 180)
# Card 1 upright dimensions: w=234, h=294
c1_unrot = orig_2x.rotate(-5.02, resample=Image.Resampling.BICUBIC, center=(131, 180))
c1_crop = c1_unrot.crop((131 - 117, 180 - 147, 131 + 117, 180 + 147))
c1_crop.save('scratch/clean_c1_upright.png')

# Card 2 (Top-center girl):
# Let's find angle of top edge of Card 2:
# In find_all_card_quads.py: Card 2 top line: y = -0.0853 * x + 48.87 -> angle = -4.87 deg
# Let's unrotate by +4.87 deg around (380, 168)
c2_unrot = orig_2x.rotate(4.87, resample=Image.Resampling.BICUBIC, center=(380, 168))
c2_crop = c2_unrot.crop((380 - 130, 168 - 155, 380 + 130, 168 + 155))
c2_crop.save('scratch/clean_c2_upright.png')

# Card 3 (Bottom guy):
# Center around (286, 396)
# Let's unrotate by -3.5 deg around (286, 396)
c3_unrot = orig_2x.rotate(-3.5, resample=Image.Resampling.BICUBIC, center=(286, 396))
c3_crop = c3_unrot.crop((286 - 135, 396 - 100, 286 + 135, 396 + 100))
c3_crop.save('scratch/clean_c3_upright.png')

# Card 4 (Right laughing girl):
# Top line: y = 0.6055 * x - 228.17 -> angle = +31.2 deg (or tilted counter-clockwise/clockwise)
# Let's find the exact tilt angle of Card 4:
# Right line: x = -0.0052 * y + 778.6 -> vertical right edge!
# Bottom line: y = 0.0887 * x + 430.8 -> angle = +5.07 deg
# Center around (610, 335)
c4_unrot = orig_2x.rotate(-5.07, resample=Image.Resampling.BICUBIC, center=(610, 335))
c4_crop = c4_unrot.crop((610 - 155, 335 - 155, 610 + 155, 335 + 155))
c4_crop.save('scratch/clean_c4_upright.png')

print("Saved all 4 upright crops.")
