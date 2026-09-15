import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Load original cards image from git commit
orig_cards = Image.open('scratch/orig_cards_binary.png').convert('RGBA')
orig_upright = Image.open('scratch/exact_orig_upright_card.png').convert('RGBA')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# In exact_orig_upright_card (144, 240):
# Let's find the exact pixel boundaries of the inner photo:
# Let's inspect where the original photo pixels are in exact_orig_upright_card
# We can find the 4 corners of the photo window:
arr = np.array(orig_upright)

# Let's test placing user_new into the photo window of exact_orig_upright_card:
# Let's crop user_new to match the photo window aspect ratio (w_photo, h_photo)
# Let's inspect different photo window bounds in exact_orig_upright_card:
# Photo window: x in [18, 126], y in [24, 178] (w=108, h=154) -> aspect ratio 0.701
# In 2x (cards.png @ 792x500):
# Photo window: x in [36, 252], y in [48, 356] (w=216, h=308)

print("user_new size:", user_new.size)
