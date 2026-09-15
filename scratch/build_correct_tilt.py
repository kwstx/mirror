import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# 1. Load the authentic true original cards image extracted from the user's reference screenshot
true_cards_1x = Image.open('scratch/true_orig_cards.png').convert('RGBA') # (395, 250)
true_cards_2x = true_cards_1x.resize((792, 500), Image.Resampling.LANCZOS) # (792, 500)
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# In 1024x425 coordinates:
# Card 1 in orig:
# TL: (317, 179) -> in cards container (top=158, left=317): TL = (0, 21)
# BL: (330, 327) -> in cards container: BL = (13, 169)
# TR: (435, 169) -> in cards container: TR = (118, 11)
# BR: (448, 317) -> in cards container: BR = (131, 159)

# Center in 1x (395, 250):
# cx = (0 + 131) / 2 = 65.5
# cy = (11 + 169) / 2 = 90.0

# Card width = distance(TL, TR) = sqrt(118^2 + 10^2) = 118.4px (in 2x: 237px)
# Card height = distance(TL, BL) = sqrt(13^2 + 148^2) = 148.6px (in 2x: 297px)
# Angle: counter-clockwise by arctan(13/148) = +5.02 degrees!

card_w_2x = 237
card_h_2x = 297
cx_2x = 65.5 * 2 # 131.0
cy_2x = 90.0 * 2 # 180.0

# 2. Crop user_new (727 x 1024) to match aspect ratio (237 / 297 = 0.798)
# For width = 727, height = 727 / 0.798 = 911:
# Crop: x in [0, 727], y in [40, 951]
crop_box = (0, 40, 727, 40 + int(727 / card_w_2x * card_h_2x))
cropped_user = user_new.crop(crop_box)

# Resize to card dimensions (237 x 297)
resized_photo = cropped_user.resize((card_w_2x, card_h_2x), Image.Resampling.LANCZOS)

# Create upright card
card_upright = Image.new('RGBA', (card_w_2x, card_h_2x), (255, 255, 255, 255))
card_upright.paste(resized_photo, (0, 0))

# Rotate by +5.02 degrees (counter-clockwise)
card_rot = card_upright.rotate(5.02, resample=Image.Resampling.BICUBIC, expand=True)
rot_w, rot_h = card_rot.size

paste_x = int(round(cx_2x - rot_w / 2))
paste_y = int(round(cy_2x - rot_h / 2))

# Create 2x canvas starting with #5a000f background
canvas = Image.new('RGBA', (792, 500), (90, 0, 15, 255))

# Soft drop shadow for Card 1
shadow_mask = card_rot.split()[3]
shadow_layer = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
shadow_stamp = Image.new('RGBA', card_rot.size, (20, 0, 5, 120))
shadow_layer.paste(shadow_stamp, (paste_x + 3, paste_y + 3), shadow_mask)
shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=2.5))

canvas.paste(shadow_layer, (0, 0), shadow_layer)
canvas.paste(card_rot, (paste_x, paste_y), card_rot)

# Overlay Cards 2, 3, 4 from true_cards_2x:
overlay_mask = Image.new('L', (792, 500), 0)
draw_mask = ImageDraw.Draw(overlay_mask)

# Points covering Cards 2, 3, 4:
poly = [
    (234, 0),
    (236, 20),
    (240, 60),
    (246, 120),
    (252, 180),
    (258, 240),
    (264, 275), # Card 2 meets Card 3
    (260, 290), # Card 3 top border
    (220, 310), # Card 3 left-top edge
    (150, 315), # Card 3 left edge
    (140, 350),
    (150, 420),
    (180, 500),
    (792, 500),
    (792, 0)
]
draw_mask.polygon(poly, fill=255)
overlay_mask = overlay_mask.filter(ImageFilter.GaussianBlur(radius=0.5))

canvas.paste(true_cards_2x, (0, 0), overlay_mask)

final_2x = canvas.convert('RGB')

# Composite onto the full 1024x425 screenshot:
full_orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGBA')
final_1x = final_2x.resize((395, 250), Image.Resampling.LANCZOS)

full_sim = full_orig.copy()
full_sim.paste(final_1x, (317, 158))
full_sim.save('scratch/corrected_full_sim.png')

print("Saved scratch/corrected_full_sim.png")
