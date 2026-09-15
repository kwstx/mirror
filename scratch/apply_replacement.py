import os
from PIL import Image, ImageDraw, ImageFilter
import shutil

cards_orig = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# Card 1 geometry
card_w, card_h = 286, 404
border = 3
photo_w, photo_h = card_w - 2 * border, card_h - 2 * border # 280 x 398

# Balanced portrait crop for user_new
# 655 x 931 crop box on 727 x 1024 source
crop_rect = (35, 15, 35 + 655, 15 + int(655 / photo_w * photo_h))

# 1. Base canvas #5a000f
canvas = Image.new('RGBA', cards_orig.size, (90, 0, 15, 255))

# 2. Crop & resize photo
cropped = user_new.crop(crop_rect)
resized = cropped.resize((photo_w, photo_h), Image.Resampling.LANCZOS)

# 3. Create polaroid card
card_upright = Image.new('RGBA', (card_w, card_h), (252, 252, 252, 255))
card_upright.paste(resized, (border, border))

# Rounded corners for polaroid
corner_mask = Image.new('L', (card_w, card_h), 255)
draw_c = ImageDraw.Draw(corner_mask)
draw_c.rounded_rectangle([(0, 0), (card_w - 1, card_h - 1)], radius=3, fill=255, outline=255)
card_upright.putalpha(corner_mask)

# 4. Rotate Card 1 (-5.0 degrees)
card_rot = card_upright.rotate(-5.0, resample=Image.Resampling.BICUBIC, expand=True)

rot_w, rot_h = card_rot.size
paste_x = int(round(159.1 - rot_w / 2))
paste_y = int(round(229.0 - rot_h / 2))

# 5. Drop shadow
shadow_mask = card_rot.split()[3]
shadow_layer = Image.new('RGBA', cards_orig.size, (0, 0, 0, 0))
shadow_stamp = Image.new('RGBA', card_rot.size, (20, 0, 5, 150))
shadow_layer.paste(shadow_stamp, (paste_x + 3, paste_y + 3), shadow_mask)
shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=3.5))

canvas.paste(shadow_layer, (0, 0), shadow_layer)
canvas.paste(card_rot, (paste_x, paste_y), card_rot)

# 6. Overlay Cards 2, 3, 4
overlay_mask = Image.new('L', cards_orig.size, 0)
draw_mask = ImageDraw.Draw(overlay_mask)
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

# Convert to RGB (to match original party_of_four_cards.png format)
final_img = canvas.convert('RGB')

# Save to public/images/
target1 = 'public/images/party_of_four_cards.png'
target2 = 'public/images/party_of_four_cards@2x.png'

final_img.save(target1, 'PNG', optimize=True)
final_img.save(target2, 'PNG', optimize=True)

# Also update dist if it exists
if os.path.exists('dist/images'):
    final_img.save('dist/images/party_of_four_cards.png', 'PNG', optimize=True)
    final_img.save('dist/images/party_of_four_cards@2x.png', 'PNG', optimize=True)

print("Successfully saved updated party_of_four_cards.png and party_of_four_cards@2x.png!")
