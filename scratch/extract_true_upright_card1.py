import os
from PIL import Image
import numpy as np

cards = Image.open('scratch/true_orig_cards.png').convert('RGBA')

# In 1x (395, 250):
# Card 1 center:
# x in [6, 135] -> cx = 70.5
# y in [11, 175] -> cy = 93.0
cx = 70.5
cy = 93.0
angle = 5.26

# Rotate cards by -5.26 to make Card 1 upright
upright_cards = cards.rotate(-angle, resample=Image.Resampling.BICUBIC, center=(cx, cy))

# Crop Card 1 in upright:
# Width: ~135, Height: ~165
crop_box = (int(cx - 68), int(cy - 83), int(cx + 68), int(cy + 83))
card1_upright = upright_cards.crop(crop_box)
card1_upright.save('scratch/true_card1_upright.png')

print("Saved true_card1_upright.png, size:", card1_upright.size)
