import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Load the original uncorrupted asset from git commit
orig_1x = Image.open('scratch/orig_cards_binary.png').convert('RGBA') # 396 x 250
orig_2x = orig_1x.resize((792, 500), Image.Resampling.LANCZOS) # 792 x 500
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# In 2x coordinates (792 x 500):
# Card 1 geometry:
# In orig_cards_binary, Card 1's exact corners in 2x:
# TL: (-1.4, 40.0) -> on canvas it starts at left edge
# TR: (282.8, 15.2)
# BR: (324.0, 487.8)
# BL: (40.0, 512.6)
# Center: cx = 161.3, cy = 263.9
# Rotation angle: -5.0 degrees (counter-clockwise 5 deg)
# Width: 285px, Height: 474px

# Let's inspect user_new (727 x 1024):
# In user_new:
# The man's head starts at y=140, chin at y=540, chest/jacket down to y=1024.
# In the original card:
# The person's head starts ~10% down, chin at ~50% down, chest down to bottom.
# To match the original framing exactly:
# Top of hair should have ~5-8% headroom.
# Width should capture shoulders.
# Target aspect ratio: 280 / 470 = 0.5957 (or including white border: 285 / 474 = 0.6013).

# Let's test a couple of natural crops of user_new (727 x 1024):
# Crop 1: (x: [20, 707], y: [40, 40 + int(687 / 0.6013)]) -> (20, 40, 707, 1024) -> (w=687, h=984) -> aspect ratio 0.698
# If aspect ratio is 285 / 474 = 0.6013:
# For w = 615, h = 615 / 0.6013 = 1022:
# Crop: x in [56, 671], y in [0, 1022]
# This captures:
# - Full head with nice wooden wall headroom above hair
# - Centered face with smile & dimples
# - Full shoulders, hoodie collar, and Carhartt jacket down to waist!

crop_exact = (56, 0, 671, 1022)
cropped_user = user_new.crop(crop_exact)

# Resize to card dimensions (285 x 474)
card_w, card_h = 285, 474
border_px = 3 # 3px authentic white border
photo_w = card_w - 2 * border_px
photo_h = card_h - 2 * border_px

resized_photo = cropped_user.resize((photo_w, photo_h), Image.Resampling.LANCZOS)

# Create upright card with white border
card_upright = Image.new('RGBA', (card_w, card_h), (250, 250, 250, 255))
card_upright.paste(resized_photo, (border_px, border_px))

# Rotate by -5.0 degrees around center
card_rot = card_upright.rotate(-5.0, resample=Image.Resampling.BICUBIC, expand=True)
rot_w, rot_h = card_rot.size

# Calculate paste position for center (cx = 161.3, cy = 263.9)
paste_x = int(round(161.3 - rot_w / 2))
paste_y = int(round(263.9 - rot_h / 2))

# Create new canvas starting from #5a000f background
canvas = Image.new('RGBA', (792, 500), (90, 0, 15, 255))

# Create drop shadow for Card 1
shadow_mask = card_rot.split()[3]
shadow_layer = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
shadow_stamp = Image.new('RGBA', card_rot.size, (20, 0, 5, 140))
shadow_layer.paste(shadow_stamp, (paste_x + 3, paste_y + 3), shadow_mask)
shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=3.5))

canvas.paste(shadow_layer, (0, 0), shadow_layer)
canvas.paste(card_rot, (paste_x, paste_y), card_rot)

# Overlay Cards 2, 3, 4 from orig_2x
overlay_mask = Image.new('L', (792, 500), 0)
draw_mask = ImageDraw.Draw(overlay_mask)

# Polygon covering Cards 2, 3, 4:
poly = [
    (246, 0),
    (246, 18),
    (249, 60),
    (252, 120),
    (255, 180),
    (258, 240),
    (261, 285),
    (268, 320),
    (280, 370),
    (300, 420),
    (325, 470),
    (345, 500),
    (792, 500),
    (792, 0)
]
draw_mask.polygon(poly, fill=255)
overlay_mask = overlay_mask.filter(ImageFilter.GaussianBlur(radius=0.5))

canvas.paste(orig_2x, (0, 0), overlay_mask)

# Save result
final_2x = canvas.convert('RGB')
final_2x.save('scratch/perfect_party_2x.png')

# Also left crop for review
final_2x.crop((0, 0, 400, 500)).save('scratch/perfect_party_left_crop.png')
print("Saved perfect_party_2x.png and perfect_party_left_crop.png")
