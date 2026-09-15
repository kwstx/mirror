import os
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import numpy as np

# Load source images
cards_orig = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')
old_user = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGBA')

# Let's inspect user_new
# Size: 727 x 1024
# Let's see what the original photo on the left was:
# The original left photo has dimensions in upright:
# Width: ~280, Height: ~398 (or ~286 x 404 including white border)
# Rotation: -5.0 degrees counter-clockwise
# Center: cx = 159.1, cy = 229.0

# Let's build candidate compositions:
# In user_new:
# The user is smiling with brown hair, wooden wall in background, Carhartt jacket.
# Let's test a few crop framings:
# Framing A: Full image cropped to target aspect ratio (0, 0, 727, 1024) -> (0, 0, 727, 1024)
# Framing B: Centered, includes from top of hair down to Carhartt logo / zipper:
#            w=680, h=966, centered
# Framing C: Nicely zoomed portrait framing head and shoulders:
#            w=620, h=881, centered horizontally, x=53, y=40

framings = {
    'A': (0, 0, 727, 1024),
    'B': (23, 20, 23 + 680, 20 + int(680 / 280 * 398)),
    'C': (53, 40, 53 + 620, 40 + int(620 / 280 * 398)),
    'D': (40, 60, 40 + 640, 60 + int(640 / 280 * 398))
}

# Let's create the composite for each framing
for label, crop_box in framings.items():
    # 1. Base canvas: start with the background color #5a000f (90, 0, 15)
    canvas = Image.new('RGBA', cards_orig.size, (90, 0, 15, 255))
    
    # 2. Prepare the upright card
    # Card outer size: 286 x 404
    card_w, card_h = 286, 404
    border = 3 # 3px white border around the photo
    photo_w = card_w - 2 * border
    photo_h = card_h - 2 * border
    
    user_cropped = user_new.crop(crop_box)
    user_resized = user_cropped.resize((photo_w, photo_h), Image.Resampling.LANCZOS)
    
    # Create upright card image
    card_upright = Image.new('RGBA', (card_w, card_h), (248, 248, 248, 255)) # clean photo paper white
    card_upright.paste(user_resized, (border, border))
    
    # Add subtle inner border/stroke if desirable or crisp photo edge
    
    # 3. Create a larger transparent surface for rotating Card 1 with shadow
    # Rotated around center (cx, cy) = (159.1, 229.0)
    card_rot = card_upright.rotate(-5.0, resample=Image.Resampling.BICUBIC, expand=True)
    
    # Create card layer with drop shadow on full canvas (792, 500)
    card_layer = Image.new('RGBA', cards_orig.size, (0, 0, 0, 0))
    # Paste card at position: top-left of rotated card
    # In find_corners.py, outer TL corner was (-0.7, 40.7), center is (159.1, 229.0)
    rot_w, rot_h = card_rot.size
    paste_x = int(round(159.1 - rot_w / 2))
    paste_y = int(round(229.0 - rot_h / 2))
    card_layer.paste(card_rot, (paste_x, paste_y), card_rot)
    
    # Create drop shadow for Card 1
    # Extract alpha mask of card_rot
    shadow_mask = card_rot.split()[3]
    shadow_layer = Image.new('RGBA', (rot_w + 20, rot_h + 20), (0, 0, 0, 0))
    # Fill shadow color (dark shadow with alpha)
    shadow_img = Image.new('RGBA', card_rot.size, (30, 0, 5, 140))
    shadow_layer.paste(shadow_img, (10, 10), shadow_mask)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=4))
    
    # Paste shadow onto canvas
    canvas.paste(shadow_layer, (paste_x - 8, paste_y - 6), shadow_layer)
    # Paste card onto canvas
    canvas.paste(card_layer, (0, 0), card_layer)
    
    # 4. Now composite the rest of the original cards (Card 2, 3, 4) ON TOP of Card 1!
    # Let's create an accurate mask of Card 2, 3, 4:
    # Everything to the right of Card 2/3's left edge
    # Let's inspect where Card 2/3 are located:
    # Card 2 left edge: x = 0.0899 * y + 235.4922 (for y in 0..320)
    # Below y=300: Card 3 top-left edge starts around (260, 290) and goes down-right
    
    # Let's build a polygon mask for the overlapping region (Cards 2, 3, 4):
    overlay_mask = Image.new('L', cards_orig.size, 0)
    draw_mask = ImageDraw.Draw(overlay_mask)
    
    # Polygon covering Card 2, 3, 4:
    # Points along Card 2 left edge:
    poly_pts = [
        (238, 0),
        (238, 20),
        (243, 60),
        (248, 120),
        (253, 180),
        (258, 240),
        (263, 295), # where Card 2 meets Card 3
        (268, 320),
        (275, 360),
        (290, 400),
        (310, 440),
        (330, 470),
        (350, 500),
        (792, 500),
        (792, 0)
    ]
    draw_mask.polygon(poly_pts, fill=255)
    
    # Feather the edge of the mask slightly (0.5px) for perfect anti-aliasing
    overlay_mask_smooth = overlay_mask.filter(ImageFilter.GaussianBlur(radius=0.7))
    
    # Composite cards_orig onto canvas using overlay_mask
    canvas.paste(cards_orig, (0, 0), overlay_mask_smooth)
    
    # Save test output
    out_path = f'scratch/candidate_party_{label}.png'
    canvas.save(out_path)
    print(f"Saved {out_path}")
