import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Load the pristine original base
orig_1x = Image.open('scratch/orig_cards_binary.png').convert('RGBA') # (396, 250)
orig_2x = orig_1x.resize((792, 500), Image.Resampling.LANCZOS) # (792, 500)
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# In 2x coordinates (792 x 500):
card_w = 284
card_h = 344

# Crop user_new (727 x 1024) to match the exact framing of the original image:
# Starting at y=50 gives top of hair at exactly 10%, eyes at 36%, chin at 55.6%:
crop_box = (0, 50, 727, 50 + int(727 / card_w * card_h)) # (0, 50, 727, 930)
cropped_user = user_new.crop(crop_box)

# Resize to card dimensions (284 x 344)
resized_card = cropped_user.resize((card_w, card_h), Image.Resampling.LANCZOS)

# Create upright card canvas with a clean crisp edge
card_upright = Image.new('RGBA', (card_w, card_h), (255, 255, 255, 255))
card_upright.paste(resized_card, (0, 0))

# Rotate by -4.95 degrees (counter-clockwise)
card_rot = card_upright.rotate(-4.95, resample=Image.Resampling.BICUBIC, expand=True)
rot_w, rot_h = card_rot.size

# Position matching original Card 1:
paste_x = -2
paste_y = 18

# Create canvas of size 792 x 500 starting with background #5a000f
canvas = Image.new('RGBA', (792, 500), (90, 0, 15, 255))

# Soft drop shadow for Card 1
shadow_mask = card_rot.split()[3]
shadow_layer = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
shadow_stamp = Image.new('RGBA', card_rot.size, (20, 0, 5, 130))
shadow_layer.paste(shadow_stamp, (paste_x + 4, paste_y + 4), shadow_mask)
shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=3.5))

canvas.paste(shadow_layer, (0, 0), shadow_layer)
canvas.paste(card_rot, (paste_x, paste_y), card_rot)

# Now composite Cards 2, 3, 4 from orig_2x:
# Using the exact border line of Card 2 and Card 3:
overlay_mask = Image.new('L', (792, 500), 0)
draw_mask = ImageDraw.Draw(overlay_mask)

poly = [
    (236, 0),
    (238, 20),
    (242, 60),
    (248, 120),
    (253, 180),
    (259, 240),
    (264, 285),
    (275, 320),
    (295, 370),
    (320, 420),
    (350, 470),
    (370, 500),
    (792, 500),
    (792, 0)
]
draw_mask.polygon(poly, fill=255)
overlay_mask = overlay_mask.filter(ImageFilter.GaussianBlur(radius=0.6))

canvas.paste(orig_2x, (0, 0), overlay_mask)

final_2x = canvas.convert('RGB')

# Save updated files to public/images and dist/images
final_2x.save('public/images/party_of_four_cards.png', 'PNG', optimize=True)
final_2x.save('public/images/party_of_four_cards@2x.png', 'PNG', optimize=True)

if os.path.exists('dist/images'):
    final_2x.save('dist/images/party_of_four_cards.png', 'PNG', optimize=True)
    final_2x.save('dist/images/party_of_four_cards@2x.png', 'PNG', optimize=True)

# Also copy to artifact dir for embedding
artifact_dir = r"C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a"
final_2x.save(os.path.join(artifact_dir, "party_of_four_cards.png"), 'PNG', optimize=True)

print("Saved exact replica to public/images and artifact directory!")
