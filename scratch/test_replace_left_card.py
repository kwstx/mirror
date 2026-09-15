import os
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import numpy as np

# Load images
cards = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# Let's inspect the exact shape of Card 1:
# In scratch/unrotate_card.py, we saw:
# cx = 159.1, cy = 229.0, theta = -5.0 degrees
# Card width: ~285px, height: ~403px
# Let's inspect the white border of Card 1 in the unrotated frame.

# Let's create an upright card canvas:
# Inside this upright card canvas:
# Outer dimensions: W_card, H_card
# White border:
# Let's measure the exact inner photo margins from unrotated card:
# In scratch/card_upright.png:
# Let's find the exact bounding box of the photo inside the white border.
