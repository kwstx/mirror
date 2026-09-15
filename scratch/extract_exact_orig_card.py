import os
from PIL import Image
import numpy as np

orig = Image.open('scratch/orig_cards_binary.png').convert('RGBA')

# In 396x250:
# Card center:
# cx = (-0.7 + 162.0) / 2 = 80.65
# cy = (7.6 + 256.3) / 2 = 131.95
cx = 80.65
cy = 131.95

# Let's rotate orig by +5.0 degrees around (cx, cy) to make it upright
unrotated_orig = orig.rotate(5.0, resample=Image.Resampling.BICUBIC, center=(cx, cy))

# Crop upright card: w=143, h=237
crop_box = (int(cx - 72), int(cy - 120), int(cx + 72), int(cy + 120))
upright_card = unrotated_orig.crop(crop_box)
upright_card.save('scratch/exact_orig_upright_card.png')
print("Saved exact_orig_upright_card.png, size:", upright_card.size)
