import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

cards_orig = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# Card 1 geometry
# Size: 286 x 404
# Angle: -5.0 degrees
# Center: cx = 159.1, cy = 229.0
card_w, card_h = 286, 404
border = 3
photo_w, photo_h = card_w - 2 * border, card_h - 2 * border # 280 x 398

# Framing options:
crops = {
    # 1. Full height/width framing (shows full jacket and wooden wall background)
    'full': (0, 0, 727, int(727 / photo_w * photo_h)),
    # 2. Balanced portrait framing (matching the original card scale and head size)
    'balanced': (35, 15, 35 + 655, 15 + int(655 / photo_w * photo_h)),
    # 3. Closer portrait framing
    'close': (60, 30, 60 + 600, 30 + int(600 / photo_w * photo_h))
}

for name, crop_rect in crops.items():
    # 1. Background canvas #5a000f
    canvas = Image.new('RGBA', cards_orig.size, (90, 0, 15, 255))
    
    # 2. Prepare card
    cropped = user_new.crop(crop_rect)
    resized = cropped.resize((photo_w, photo_h), Image.Resampling.LANCZOS)
    
    card_upright = Image.new('RGBA', (card_w, card_h), (252, 252, 252, 255))
    card_upright.paste(resized, (border, border))
    
    # Optional: subtle rounded corners on the card (e.g. 2px radius)
    # The original polaroid cards have crisp slightly rounded corners
    corner_mask = Image.new('L', (card_w, card_h), 255)
    draw_c = ImageDraw.Draw(corner_mask)
    # 2px rounded corners
    draw_c.rounded_rectangle([(0, 0), (card_w - 1, card_h - 1)], radius=3, fill=255, outline=255)
    card_upright.putalpha(corner_mask)
    
    # 3. Rotate Card 1
    # Rotate by -5.0 degrees with bicubic interpolation
    card_rot = card_upright.rotate(-5.0, resample=Image.Resampling.BICUBIC, expand=True)
    
    rot_w, rot_h = card_rot.size
    paste_x = int(round(159.1 - rot_w / 2))
    paste_y = int(round(229.0 - rot_h / 2))
    
    # 4. Drop shadow
    shadow_mask = card_rot.split()[3]
    shadow_layer = Image.new('RGBA', cards_orig.size, (0, 0, 0, 0))
    
    # Card shadow (soft dark red/black shadow)
    shadow_stamp = Image.new('RGBA', card_rot.size, (20, 0, 5, 150))
    # Offset shadow by (4, 4) down-right
    shadow_layer.paste(shadow_stamp, (paste_x + 3, paste_y + 3), shadow_mask)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=3.5))
    
    canvas.paste(shadow_layer, (0, 0), shadow_layer)
    
    # 5. Paste Card 1
    canvas.paste(card_rot, (paste_x, paste_y), card_rot)
    
    # 6. Overlay Cards 2, 3, 4
    # Let's create the precise mask for Cards 2, 3, 4
    overlay_mask = Image.new('L', cards_orig.size, 0)
    draw_mask = ImageDraw.Draw(overlay_mask)
    
    # Precise polygon following Card 2 left border and Card 3 border:
    # Card 2 left edge goes from (248, 18) down to (254, 280)
    # Card 3 top-left edge goes from (254, 280) to (270, 310) down to (290, 480)
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
    
    canvas.paste(cards_orig, (0, 0), overlay_mask)
    
    out_file = f'scratch/final_candidate_{name}.png'
    canvas.save(out_file)
    print(f"Generated {out_file}")
