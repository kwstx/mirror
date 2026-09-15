import os
from PIL import Image
import numpy as np

orig = Image.open('scratch/orig_cards_binary.png').convert('RGB')
user_crop = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')

print("orig size:", orig.size)
print("user_crop size:", user_crop.size)

# Let's save orig to scratch for inspection
orig.save('scratch/orig_cards_view.png')

# Let's compare user_crop with orig:
# In orig (396, 250):
# Where is the left card in orig?
# Let's inspect the left card in orig:
# It's at x: [0, 180], y: [0, 250]
orig_left = orig.crop((0, 0, 180, 250))
orig_left.save('scratch/orig_left_card.png')

print("Saved scratch/orig_left_card.png")
