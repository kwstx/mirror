import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# 1. Load the authentic true original cards image extracted from the user's reference screenshot
true_cards_1x = Image.open('scratch/true_orig_cards.png').convert('RGBA') # (395, 250)
true_cards_2x = true_cards_1x.resize((792, 500), Image.Resampling.LANCZOS) # (792, 500)
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# 2. In 1x (395, 250):
# Card 1 center: cx = 70.5, cy = 93.0
# Card 1 angle: +5.26 degrees (or -5.26 degrees in rotate)
# Card 1 width: 126px, height: 150px
# In 2x (792, 500):
cx_2x = 70.5 * 2 # 141.0
cy_2x = 93.0 * 2 # 186.0
card_w_2x = 126 * 2 # 252
card_h_2x = 150 * 2 # 300

# 3. Crop user_new (727 x 1024) to match the exact aspect ratio (252 / 300 = 0.84)
# In the original Card 1 (blond guy in beige shirt):
# Top of hair is at ~10% from top of card.
# Chin is at ~55% from top of card.
# Chest / beige shirt fills lower half down to bottom edge.
# In user_new (727 x 1024):
# Top of hair is at y=140, chin at y=540, chest down to y=1024.
# For aspect ratio 252 / 300 = 0.84:
# If width = 727, height = 727 / 0.84 = 865.5.
# Crop from y=30 to y=30+865 = y=895:
# Top of hair: (140 - 30) / 865 = 110 / 865 = 12.7% (matching original!).
# Chin: (540 - 30) / 865 = 510 / 865 = 58.9% (matching original!).
# Carhartt jacket fills lower half down to bottom.
crop_box = (0, 30, 727, 30 + int(727 / card_w_2x * card_h_2x))
cropped_user = user_new.crop(crop_box)

# Resize to card dimensions (252 x 300)
resized_photo = cropped_user.resize((card_w_2x, card_h_2x), Image.Resampling.LANCZOS)

# Create upright card
card_upright = Image.new('RGBA', (card_w_2x, card_h_2x), (255, 255, 255, 255))
card_upright.paste(resized_photo, (0, 0))

# Rotate by -5.26 degrees around center (cx_2x, cy_2x)
# In PIL rotate positive is counter-clockwise, so -5.26 rotates clockwise by 5.26 deg
card_rot = card_upright.rotate(-5.26, resample=Image.Resampling.BICUBIC, expand=True)
rot_w, rot_h = card_rot.size

paste_x = int(round(cx_2x - rot_w / 2))
paste_y = int(round(cy_2x - rot_h / 2))

# Create full 2x canvas starting with #5a000f background
canvas = Image.new('RGBA', (792, 500), (90, 0, 15, 255))

# Subtle drop shadow for Card 1
shadow_mask = card_rot.split()[3]
shadow_layer = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
shadow_stamp = Image.new('RGBA', card_rot.size, (20, 0, 5, 120))
shadow_layer.paste(shadow_stamp, (paste_x + 3, paste_y + 3), shadow_mask)
shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=2.5))

canvas.paste(shadow_layer, (0, 0), shadow_layer)
canvas.paste(card_rot, (paste_x, paste_y), card_rot)

# Overlay Cards 2, 3, 4 from true_cards_2x:
# Using the exact border line of Card 2 and Card 3:
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
final_2x.save('scratch/true_exact_replica_2x.png')

# Also composite onto the full 1024x425 screenshot to compare directly with user's media_1789475594670.png!
full_orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGBA')
final_1x = final_2x.resize((395, 250), Image.Resampling.LANCZOS)

full_sim = full_orig.copy()
full_sim.paste(final_1x, (317, 158))
full_sim.save('scratch/simulated_full_page.png')

print("Saved scratch/true_exact_replica_2x.png and scratch/simulated_full_page.png")
