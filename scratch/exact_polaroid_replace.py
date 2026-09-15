import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Load the authentic original cards image
orig_1x = Image.open('scratch/orig_cards_binary.png').convert('RGBA')
orig_2x = orig_1x.resize((792, 500), Image.Resampling.LANCZOS)
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# 1. Unrotate orig_2x by +5.0 degrees around Card 1 center (cx_2x, cy_2x)
cx_2x = 80.65 * 2 # 161.3
cy_2x = 131.95 * 2 # 263.9

# We create an upright version of the whole canvas (or Card 1 area)
upright_2x = orig_2x.rotate(5.0, resample=Image.Resampling.BICUBIC, center=(cx_2x, cy_2x))

# 2. In upright_2x, the Card 1 crop top-left is at (int(cx_2x - 144), int(cy_2x - 240)) = (17, 23)
card_tl_x = int(cx_2x - 144) # 17
card_tl_y = int(cy_2x - 240) # 23

# Photo window relative to Card 1 top-left:
# x in [52, 228], y in [56, 304] -> absolute coordinates in upright_2x:
photo_abs_x = card_tl_x + 52 # 69
photo_abs_y = card_tl_y + 56 # 79
photo_w = 228 - 52 # 176
photo_h = 304 - 56 # 248

# 3. Resize user_new to (photo_w, photo_h)
user_resized = user_new.resize((photo_w, photo_h), Image.Resampling.LANCZOS)

# 4. Paste user_resized into upright_2x with subtle anti-aliased edge mask
# Create soft edge mask for seamless integration into polaroid frame
mask = Image.new('L', (photo_w, photo_h), 255)
# Paste onto upright_2x
upright_2x.paste(user_resized, (photo_abs_x, photo_abs_y), mask)

# 5. Rotate upright_2x back by -5.0 degrees
new_cards_2x = upright_2x.rotate(-5.0, resample=Image.Resampling.BICUBIC, center=(cx_2x, cy_2x))

# 6. To guarantee that Cards 2, 3, 4 and the background outside Card 1 are 100% pristine:
# Composite orig_2x over new_cards_2x for all pixels belonging to Cards 2, 3, 4
# Mask for Cards 2, 3, 4:
overlay_mask = Image.new('L', (792, 500), 0)
draw_mask = ImageDraw.Draw(overlay_mask)

# Points covering Cards 2, 3, 4:
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

new_cards_2x.paste(orig_2x, (0, 0), overlay_mask)

# Also create 1x version:
new_cards_1x = new_cards_2x.resize((396, 250), Image.Resampling.LANCZOS)

# Save results to scratch
new_cards_2x.convert('RGB').save('scratch/exact_placed_cards_2x.png')
new_cards_1x.convert('RGB').save('scratch/exact_placed_cards_1x.png')

# Save crop of left card for inspection
new_cards_2x.crop((0, 0, 400, 500)).save('scratch/exact_placed_left_crop.png')
print("Saved exact_placed_cards_2x.png and exact_placed_left_crop.png")
