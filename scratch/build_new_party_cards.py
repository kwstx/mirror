import os
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import numpy as np

# Load base assets
cards_orig = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')
old_user = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGBA')

# Let's inspect the exact position and rotation of Card 1
# Card 1 outer dimensions: width = 286, height = 404
# Angle: -5.0 degrees (counter-clockwise 5 degrees)
# Center: cx = 159, cy = 229

# Let's test different framings of user_new:
# user_new is 727 x 1024
# We can crop user_new to target aspect ratio (280 / 398 = 0.7035)
target_w, target_h = 280, 398
border_thickness = 3 # 3px white border around photo -> total card: 286 x 404

# In user_new (727 x 1024):
# The person's face is in the upper-middle area.
# Let's create a few framing options:
# Option 1: Standard crop (slight top padding above hair, includes chest and Carhartt logo)
# Option 2: Closer crop on face/shoulders
# Option 3: Slightly wider crop

def create_card(crop_box_user, border_w=3):
    # Crop user_new
    cropped = user_new.crop(crop_box_user)
    # Resize to inner photo size
    photo_w = 286 - 2 * border_w
    photo_h = 404 - 2 * border_w
    photo = cropped.resize((photo_w, photo_h), Image.Resampling.LANCZOS)
    
    # Create card with white border
    card = Image.new('RGBA', (286, 404), (255, 255, 255, 255))
    card.paste(photo, (border_w, border_w))
    return card

# Let's test different crop boxes of user_new (727 x 1024)
# Target aspect ratio: 280 / 398 = 0.7035
# Box 1: full width (0, 0, 727, 727 / 0.7035 = 1033 -> 0, 0, 727, 1024)
crop1 = (0, 0, 727, int(727 / (photo_w := 280) * (photo_h := 398))) # (0, 0, 727, 1024)
# Box 2: slightly zoomed in on upper body (30, 20, 727-30, 20 + int((727-60)/280*398))
w2 = 660
h2 = int(w2 / 280 * 398)
crop2 = (33, 30, 33 + w2, 30 + h2)

# Box 3: tighter framing
w3 = 600
h3 = int(w3 / 280 * 398)
crop3 = (63, 60, 63 + w3, 60 + h3)

print("Crop1:", crop1)
print("Crop2:", crop2)
print("Crop3:", crop3)

# Let's build full collage for each option
# How to combine Card 1 with the rest of cards_orig:
# 1. Start with blank canvas of size 792 x 500 with background color #5a000f (90, 0, 15)
# 2. Add drop shadow for Card 1
# 3. Paste rotated Card 1
# 4. Composite Card 2, 3, 4 from cards_orig over Card 1

# Let's find the exact mask of Card 2 & 3 that sit ON TOP of Card 1:
# In cards_orig, where does Card 2 & 3 overlap Card 1?
# Card 2 has a top-left corner around (248, 18), left edge sloping down to (270, 300)
# Let's detect the mask of everything to the right of Card 1's non-overlapping region!
