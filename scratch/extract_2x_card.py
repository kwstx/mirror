import os
from PIL import Image, ImageDraw
import numpy as np

orig_cards = Image.open('scratch/orig_cards_binary.png').convert('RGBA')
orig_2x = orig_cards.resize((792, 500), Image.Resampling.LANCZOS)
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# In orig_cards (396, 250):
# Center of Card 1: (80.65, 131.95)
# Rotation: -5.0 degrees
# Let's rotate orig_cards by +5.0 degrees around (80.65, 131.95)
cx_1x, cy_1x = 80.65, 131.95
orig_upright_1x = orig_cards.rotate(5.0, resample=Image.Resampling.BICUBIC, center=(cx_1x, cy_1x))

# In 2x (792, 500):
cx_2x, cy_2x = cx_1x * 2, cy_1x * 2 # (161.3, 263.9)
orig_upright_2x = orig_2x.rotate(5.0, resample=Image.Resampling.BICUBIC, center=(cx_2x, cy_2x))

# Let's inspect the photo window in 2x:
# Card crop in 2x:
card_2x_crop = orig_upright_2x.crop((int(cx_2x - 144), int(cy_2x - 240), int(cx_2x + 144), int(cy_2x + 240)))
card_2x_crop.save('scratch/card_2x_upright.png')
print("Saved card_2x_upright.png, size:", card_2x_crop.size)
