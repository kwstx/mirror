import os
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import numpy as np

# Load original 2x cards (792 x 500)
orig_2x = Image.open('scratch/true_orig_cards.png').convert('RGBA').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)
bg = np.array([90, 0, 15], dtype=float)

# Let's construct clean geometric polygons for each card:
# Card 1 (Left):
# TL: (18, 26), TR: (246, 12), BR: (264, 322), BL: (36, 336)
poly_c1 = [(18, 26), (246, 12), (264, 322), (36, 336)]

# Card 2 (Center-Top):
# TL: (246, 26), TR: (510, 6), BR: (526, 314), BL: (262, 334)
poly_c2 = [(246, 26), (510, 6), (526, 314), (262, 334)]

# Card 3 (Center-Bottom):
# TL: (152, 314), TR: (414, 292), BR: (430, 492), BL: (168, 499)
poly_c3 = [(152, 314), (414, 292), (430, 492), (168, 499)]

# Card 4 (Right):
# TL: (456, 178), TR: (780, 198), BR: (752, 496), BL: (430, 476)
poly_c4 = [(456, 178), (780, 198), (752, 496), (430, 476)]

# Combined card mask:
full_mask = Image.new('L', (792, 500), 0)
draw = ImageDraw.Draw(full_mask)
draw.polygon(poly_c1, fill=255)
draw.polygon(poly_c2, fill=255)
draw.polygon(poly_c3, fill=255)
draw.polygon(poly_c4, fill=255)

# Also let's inspect the actual non-bg mask in orig_2x to refine the polygons:
diff = np.linalg.norm(arr[:, :, :3].astype(float) - bg, axis=2)
# Any pixel with diff > 30 is card content
card_content_mask = diff > 30

# Morphological closing / filling:
from scipy.ndimage import binary_fill_holes, binary_erosion, binary_dilation
filled_mask = binary_fill_holes(card_content_mask)

# Erode by 2 pixels to completely remove ANY red background fringe on outer boundaries:
eroded_mask = binary_erosion(filled_mask, iterations=2)

# Save mask visualization
Image.fromarray((eroded_mask * 255).astype(np.uint8)).save('scratch/eroded_cards_mask.png')
print("Saved eroded_cards_mask.png")
