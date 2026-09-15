import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Load the 4 upright card crops
c1 = Image.open('scratch/clean_c1_upright.png').convert('RGBA')
c2 = Image.open('scratch/clean_c2_upright.png').convert('RGBA')
c3 = Image.open('scratch/clean_c3_upright.png').convert('RGBA')
c4 = Image.open('scratch/clean_c4_upright.png').convert('RGBA')

# Let's inspect the dimensions of each upright crop:
# c1: (234, 294)
# c2: (260, 310)
# c3: (270, 200)
# c4: (310, 310)

# For each card, we create a clean polaroid/photo card:
# 1. Inward crop to remove all outer edge bleed:
# 2. Add a clean solid white border
# 3. Rotate and paste at exact coordinates

def make_clean_card(img, margin_crop=4, border_white=3):
    # Crop inward by margin_crop
    w, h = img.size
    inner = img.crop((margin_crop, margin_crop, w - margin_crop, h - margin_crop))
    
    # Create white card frame
    card = Image.new('RGBA', (inner.width + 2 * border_white, inner.height + 2 * border_white), (255, 255, 255, 255))
    card.paste(inner, (border_white, border_white))
    return card

# Card 1:
card1 = make_clean_card(c1, margin_crop=6, border_white=4)
# Card 2:
card2 = make_clean_card(c2, margin_crop=6, border_white=4)
# Card 3:
card3 = make_clean_card(c3, margin_crop=6, border_white=4)
# Card 4:
card4 = make_clean_card(c4, margin_crop=6, border_white=4)

# Create full 2x canvas (792 x 500)
canvas = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
shadow_canvas = Image.new('RGBA', (792, 500), (0, 0, 0, 0))

# Positions and angles:
# Card 1: cx = 131, cy = 180, angle = +5.02 deg
# Card 2: cx = 380, cy = 168, angle = -4.87 deg
# Card 3: cx = 286, cy = 396, angle = +3.5 deg
# Card 4: cx = 610, cy = 335, angle = +5.07 deg (or -5.07 deg)

cards_spec = [
    (card1, 131, 180, 5.02),
    (card2, 380, 168, -4.87),
    (card3, 286, 396, 3.5),
    (card4, 610, 335, 5.07)
]

for card_img, cx, cy, angle in cards_spec:
    # Rotate card with bicubic resampling
    rot = card_img.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    rw, rh = rot.size
    px = int(round(cx - rw / 2))
    py = int(round(cy - rh / 2))
    
    # Shadow for this card
    s_mask = rot.split()[3]
    s_stamp = Image.new('RGBA', rot.size, (0, 0, 0, 45)) # light soft black shadow
    s_layer = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
    s_layer.paste(s_stamp, (px + 2, py + 3), s_mask)
    s_blur = s_layer.filter(ImageFilter.GaussianBlur(radius=4))
    
    # Paste shadow then card onto canvas
    canvas.paste(s_blur, (0, 0), s_blur)
    canvas.paste(rot, (px, py), rot)

# Test on pure white background
test_white = Image.new('RGB', (792, 500), (255, 255, 255))
test_white.paste(canvas, (0, 0), canvas)

test_white.save('scratch/perfect_clean_white_test.png')
canvas.save('scratch/perfect_clean_trans.png')

print("Saved perfect_clean_white_test.png and perfect_clean_trans.png")
