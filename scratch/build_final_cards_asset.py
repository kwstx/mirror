import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# 1. Load the authentic true original cards image extracted from user's full screenshot
true_cards_1x = Image.open('scratch/true_orig_cards.png').convert('RGBA') # (395, 250)
true_cards_2x = true_cards_1x.resize((792, 500), Image.Resampling.LANCZOS) # (792, 500)
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# In 2x coordinates (792 x 500):
# Card dimensions: width = 238px, height = 298px
# Center: cx = 131.0, cy = 180.0
# Rotation: +5.02 degrees (counter-clockwise)
card_w = 238
card_h = 298
cx = 131.0
cy = 180.0
angle = 5.02
border_w = 4 # 4px authentic white border in 2x (2px in 1x)

# Photo dimensions inside white border:
photo_w = card_w - 2 * border_w
photo_h = card_h - 2 * border_w

# 2. Crop user_new (727 x 1024) to match the exact portrait framing of the original
# Head centered, slight headroom above hair (10%), face and smile centered, Carhartt jacket fills lower body
crop_box = (0, 35, 727, 35 + int(727 / photo_w * photo_h))
cropped_user = user_new.crop(crop_box)
resized_photo = cropped_user.resize((photo_w, photo_h), Image.Resampling.LANCZOS)

# 3. Create upright card with clean white border
card_upright = Image.new('RGBA', (card_w, card_h), (252, 252, 252, 255))
card_upright.paste(resized_photo, (border_w, border_w))

# Subtle 2px rounded corners on the photo card
corner_mask = Image.new('L', (card_w, card_h), 255)
draw_c = ImageDraw.Draw(corner_mask)
draw_c.rounded_rectangle([(0, 0), (card_w - 1, card_h - 1)], radius=3, fill=255, outline=255)
card_upright.putalpha(corner_mask)

# 4. Rotate by +5.02 degrees (counter-clockwise)
card_rot = card_upright.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
rot_w, rot_h = card_rot.size

paste_x = int(round(cx - rot_w / 2))
paste_y = int(round(cy - rot_h / 2))

# 5. Base canvas (792 x 500) #5a000f
canvas = Image.new('RGBA', (792, 500), (90, 0, 15, 255))

# Ambient drop shadow matching original
shadow_mask = card_rot.split()[3]
shadow_layer = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
shadow_stamp = Image.new('RGBA', card_rot.size, (20, 0, 5, 130))
shadow_layer.paste(shadow_stamp, (paste_x + 3, paste_y + 3), shadow_mask)
shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=2.5))

canvas.paste(shadow_layer, (0, 0), shadow_layer)
canvas.paste(card_rot, (paste_x, paste_y), card_rot)

# 6. Composite Cards 2, 3, 4 from true_cards_2x cleanly on top:
overlay_mask = Image.new('L', (792, 500), 0)
draw_mask = ImageDraw.Draw(overlay_mask)

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

# Save to public/images and dist/images
final_2x.save('public/images/party_of_four_cards.png', 'PNG', optimize=True)
final_2x.save('public/images/party_of_four_cards@2x.png', 'PNG', optimize=True)

if os.path.exists('dist/images'):
    final_2x.save('dist/images/party_of_four_cards.png', 'PNG', optimize=True)
    final_2x.save('dist/images/party_of_four_cards@2x.png', 'PNG', optimize=True)

# Copy to artifact directory for presentation
artifact_dir = r"C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a"
final_2x.save(os.path.join(artifact_dir, "party_of_four_cards.png"), 'PNG', optimize=True)

print("Saved authentic final image assets!")
